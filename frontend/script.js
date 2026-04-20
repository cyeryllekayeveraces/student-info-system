const API = "http://127.0.0.1:5000/students";
let editingId = null;

// LOAD
function loadStudents() {
  fetch(API)
    .then(res => res.json())
    .then(data => {
      let table = document.getElementById("studentTable");
      table.innerHTML = "";

      data.forEach(s => {
        table.innerHTML += `
          <tr>
            <td>${s.student_id}</td>
            <td>${s.first_name} ${s.last_name}</td>
            <td>${s.course_name}</td>
            <td>
              <button onclick="editStudent('${s.student_id}')">Edit</button>
              <button onclick="deleteStudent('${s.student_id}')">Delete</button>
            </td>
          </tr>
        `;
      });
    });
}

// ADD / UPDATE
function addStudent() {
  const student = {
    student_id: document.getElementById("student_id").value,
    first_name: document.getElementById("first_name").value,
    last_name: document.getElementById("last_name").value,
    gender: document.getElementById("gender").value,
    birthdate: document.getElementById("birthdate").value,
    address: document.getElementById("address").value,
    contact_number: document.getElementById("contact_number").value,
    course_id: document.getElementById("course_id").value,
    course_name: document.getElementById("course_name").value,
    course_code: document.getElementById("course_code").value,
    enrollment_id: document.getElementById("enrollment_id").value
  };

  if (editingId) {
    fetch(`${API}/${editingId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(student)
    })
    .then(res => res.json())
    .then(() => {
      editingId = null;
      clearForm();
      loadStudents();
    });
  } else {
    fetch(API, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(student)
    })
    .then(res => res.json())
    .then(() => {
      clearForm();
      loadStudents();
    });
  }
}

// EDIT
function editStudent(id) {
  fetch(API)
    .then(res => res.json())
    .then(data => {
      const s = data.find(stu => stu.student_id === id);

      document.getElementById("student_id").value = s.student_id;
      document.getElementById("first_name").value = s.first_name;
      document.getElementById("last_name").value = s.last_name;
      document.getElementById("gender").value = s.gender;
      document.getElementById("birthdate").value = s.birthdate;
      document.getElementById("address").value = s.address;
      document.getElementById("contact_number").value = s.contact_number;
      document.getElementById("course_id").value = s.course_id;
      document.getElementById("course_name").value = s.course_name;
      document.getElementById("course_code").value = s.course_code;
      document.getElementById("enrollment_id").value = s.enrollment_id;

      editingId = id;
    });
}

// DELETE
function deleteStudent(id) {
  fetch(`${API}/${id}`, { method: "DELETE" })
    .then(() => loadStudents());
}

// SEARCH
function searchStudent() {
  const input = document.getElementById("search").value.toLowerCase();
  const rows = document.querySelectorAll("#studentTable tr");

  rows.forEach(row => {
    const name = row.children[1].innerText.toLowerCase();
    row.style.display = name.includes(input) ? "" : "none";
  });
}

// CLEAR FORM
function clearForm() {
  document.querySelectorAll(".form input").forEach(i => i.value = "");
}

// AUTO LOAD
loadStudents();
