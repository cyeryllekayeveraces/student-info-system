
function login() {
  document.getElementById("login").style.display = "none";
  document.getElementById("dashboard").style.display = "block";
}

function logout() {
  document.getElementById("dashboard").style.display = "none";
  document.getElementById("login").style.display = "block";
}

function showGrades() {
  document.getElementById("grades").style.display = "block";
}