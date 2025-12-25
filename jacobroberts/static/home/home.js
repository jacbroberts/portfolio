const d = new Date();
let year = d.getFullYear();
document.getElementById("copyYear").innerHTML = '&copy ' + year;

current = window.location.href;
current = current.split("/");

current = current.at(-1);
if (current === "")
{
    current = "home";
}


document.getElementById(current).classList.add("current");

