async function uploadAudio() {
    const fileInput = document.getElementById("audioFile");

    if (!fileInput.files.length) {
        alert("Chọn file trước!");
        return;
    }

    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append("file", file);

    document.getElementById("status").innerText =
        "Đang upload...";

    try {

        const response = await fetch(
            "https://ai-detected-notes-and-change-to-sheet.onrender.com/upload",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        console.log(data);

        document.getElementById("status").innerText =
            "Hoàn thành!";

    } catch (error) {

        console.error(error);

        document.getElementById("status").innerText =
            "Lỗi!";
    }
}