

console.log('inside fetch example');


function getUsers(){
    console.log('clicked');
    x = document.forms['get-user']['number'].value;
    fetch("https://reqres.in/api/users/" + x).then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(user) {
    // console.log(response_obj_data);
    if (!user) {
        alert('Could not find user');
        return;
    }

    const curr_main = document.querySelector("main");
    const section = document.createElement('section');
    section.innerHTML = `
    <img src="${user.avatar}" alt="Profile Picture"/>
    <div>
        <span>${user.first_name} ${user.last_name}</span>
        <br>
        <a href="mailto:${user.email}">Send Email</a>
    </div>
    `;
    curr_main.appendChild(section);
}