const express = require("express");
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = "/calculator";

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get("/greeting", (req, res) => {
  return res.send("Hello world!");
});

baseRouter.post("/add", (req, res) => {
  data = req.body;
  res.status(200).send({ result: data["first"] + data["second"] });
});

baseRouter.post("/subtract", (req, res) => {
  data = req.body;
  res.status(200).send({ result: data["first"] - data["second"] });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
  console.log("Server running at PORT", PORT);
});
