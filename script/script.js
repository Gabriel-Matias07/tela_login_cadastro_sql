async function addUser() {
    let name = document.getElementById("name").value;
    const response = await fetch("http://127.0.0.1:5000/add_user", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: name })
    });
    const result = await response.json();
    alert(result.message);
    getUsers();
}

async function getUsers() {
    const response = await fetch("http://127.0.0.1:5000/users");
    const users = await response.json();

    let userList = document.getElementById("user-list");
    userList.innerHTML = "";
    users.forEach(user => {
        let li = document.createElement("li");
        li.textContent = `${user.id} - ${user.name}`;
        userList.appendChild(li);
    });    
}

getUsers(); // Carrega a lista ao iniciar