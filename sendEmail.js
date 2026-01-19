import express from "express";
import Router from "express";
const route = Router();
import admin from "../../firebase/admin.js";
import { createTransport } from "nodemailer";
import sgMail from "@sendgrid/mail";
import { createClient } from "redis";
sgMail.setApiKey(process.env.SENDGRID_API_KEY_SPPU);

const opts = {
  host: process.env.REDIS_HOST ?? "127.0.0.1",
  port: process.env.REDIS_PORT ?? 6379,
  url: process.env.REDIS_URL
};

const client = createClient(opts)
await client.connect();
const defaultTransporter = createTransport({
  host: "smtp.gmail.com",
  port: 465,
  secure: true,
  auth: {
    user: process.env.DEFAULT_USER,
    pass: process.env.DEFAULT_PASSWORD,
  },
});

export default (app) => {
  app.use("/sendEmail", route); 
  route.post("/sendEmailTest", async(req, res) => {

  })
  route.post("/send", async (req, res) => {
    const { senderMail, senderMailPassword, to, host, subject, body } =
      req.body;
    try {
      if (to !== undefined && body !== undefined) {
        let transporter;
        if (host === "smtp.gmail.com") {
          transporter = createTransport({
            host: host,
            port: 465,
            secure: true,
            auth:
              senderMail && senderMailPassword
                ? {
                  user: senderMail,
                  pass: senderMailPassword,
                }
                : {
                  user: process.env.DEFAULT_USER,
                  pass: process.env.DEFAULT_PASSWORD,
                },
          });
        } else {
          transporter = createTransport({
            host: host,
            port: 587,
            secure: false,
            auth:
              senderMail && senderMailPassword
                ? {
                  user: senderMail,
                  pass: senderMailPassword,
                }
                : {
                  user: process.env.DEFAULT_USER,
                  pass: process.env.DEFAULT_PASSWORD,
                },
          });
        }
        const mailOptions = {
          to: to,
          from: senderMail,
          subject: subject ?? "",
          html: body,
        };
        transporter.sendMail(mailOptions, function (error, info) {
          if (error) {
            console.error("error", error);
            defaultTransporter.sendMail(mailOptions, (error, info) => {
              if (error) console.error(error);
            });
          } else {
            console.log("info", info);
          }
        });
        return res.status(200).end();
      } else {
        const data = "Required fields not present";
        return res.status(301).json({ data }).end();
      }
    } catch (e) {
      return res.status(500).end();
    }
  });
  route.post("/sendBulkMail", async (req, res) => {
    const { senderMail, senderMailPassword, host, subject, users } = req.body;
    try {
      sendBulkMail(users, host, senderMail, senderMailPassword, subject);
      return res.status(200).end();
    } catch (e) {
      return res.status(500).end();
    }
  });
};
const promisifySendMail = (transporter, mailOptions) => {
  return new Promise((resolve, reject) => {
    transporter.sendMail(mailOptions, (error, info) => {
      if (error) {
        console.error("error", error);
        reject(error);
      } else {
        console.log("info", info);
        resolve(info);
      }
    });
  });
};
export const sendBulkMail = async (users, host, senderMail, senderMailPassword, subject, body) => {
  if(users[0].instituteId === 'aeb2dd8e-bb6f-436a-945e-fb1c39e1b6c3'){ 
    let bulkEmails = [];
    for (let i = 0; i < users.length; i++) {
      const element = users[i];
      if (element.email !== "") {
        bulkEmails.push({
          to: element.email,
          from: senderMail,
          subject: subject ?? "",
          html: element.body,
        });
      }
      users = users.slice(1)
      i--
      if (users.length === 0)  {
        await client.del("notificationQueue");
      }
    }
    try {
      await sgMail.send(bulkEmails)
      await client.del("notificationQueue");
      if (users.length > 0) await redis.set('notificationQueue', JSON.stringify(users))      
    } catch (error) {
      console.error(error)
    }
  }
  else{
    let promises = [];
    for (let i = 0; i < users.length; i++) {
      const element = users[i];
      if (element.email !== "") {
        let transporter;
        if (host === "smtp.gmail.com") {
          transporter = createTransport({
            host: host,
            port: 465,
            secure: true,
            auth: senderMail && senderMailPassword
              ? {
                user: senderMail,
                pass: senderMailPassword,
              }
              : {
                user: process.env.DEFAULT_USER,
                pass: process.env.DEFAULT_PASSWORD,
              },
          });
        } else {
          transporter = createTransport({
            host: host,
            port: 587,
            secure: false,
            auth: senderMail && senderMailPassword
              ? {
                user: senderMail,
                pass: senderMailPassword,
              }
              : {
                user: process.env.DEFAULT_USER,
                pass: process.env.DEFAULT_PASSWORD,
              },
          });
        }
        const mailOptions = {
          to: element.email,
          from: senderMail,
          subject: subject ?? "",
          html: element.body,
        };
        let promise = await promisifySendMail(transporter, mailOptions);
        promises.push(promise);
      }
      users = users.slice(1)
      i--
      if (users.length === 0)  {
        await client.del("notificationQueue");
      }
    }
    try {
      await Promise.all(promises);
      await client.del("notificationQueue");
      if (users.length > 0) await redis.set('notificationQueue', JSON.stringify(users))
      
    } catch (error) {
      console.error(error)
    }
  
  }
}