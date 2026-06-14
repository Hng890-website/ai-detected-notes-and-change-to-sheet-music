async function uploadFile(){

    const file =
        document.getElementById("audioFile").files[0];

    if(!file){
        alert("Chọn file trước!");
        return;
    }

    const formData = new FormData();
    formData.append("audio", file);

    const response =
        await fetch("/upload", {
            method:"POST",
            body:formData
        });

    const data = await response.json();

    document.getElementById("result")
        .innerHTML =
        `<h3>${data.message}</h3>`;
}