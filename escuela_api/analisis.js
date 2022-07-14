import fetch from "node-fetch";
const respuesta = fetch("http://127.0.0.1:5000/datos");
respuesta.then((r) => r.json().then((j) => console.log(j)));
