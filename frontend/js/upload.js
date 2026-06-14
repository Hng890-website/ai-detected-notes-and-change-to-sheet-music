const btn =
document.getElementById("uploadBtn");

btn.addEventListener("click", () => {

    const file =
    document.getElementById("audioFile")
    .files[0];

    if(!file){
        alert("Chọn file trước!");
        return;
    }

    document.getElementById("status")
    .textContent =
    `Đã chọn: ${file.name}`;
});