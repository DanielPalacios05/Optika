// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.9.4/firebase-app.js";
import {
  getStorage,
  ref,
  uploadBytes,
} from "https://www.gstatic.com/firebasejs/9.9.4/firebase-storage.js";

const firebaseConfig = {
  apiKey: "AIzaSyBBCioy9g_Vd5o8l8NCQ3iPXu6tVGfil0c",
  authDomain: "optika-6e7bd.firebaseapp.com",
  databaseURL: "https://optika-6e7bd-default-rtdb.firebaseio.com",
  projectId: "optika-6e7bd",
  storageBucket: "optika-6e7bd.appspot.com",
  messagingSenderId: "101731463535",
  appId: "1:101731463535:web:6305f94fa27c289e8e389a",
  measurementId: "G-1LJ84D06HZ",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

document.getElementById("form").addEventListener("submit", uploadimage);

function uploadimage(e) {
  e.preventDefault();
  var file = document.getElementById("picture").files[0];
  var storage = getStorage();
  var storageRef = ref(storage, "images/" + file.name);
  uploadBytes(storageRef, file).then((snapshot) => {
    console.log("Uploaded a file!");
  });
}
