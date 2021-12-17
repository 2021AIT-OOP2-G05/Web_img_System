function previewImage(obj){
    var fileReader = new FileReader();
    fileReader.onload = (function() {
        var canvas = document.getElementById('preview');
        var ctx = canvas.getContext('2d');
        var image = new Image();
        image.src = fileReader.result;
        image.onload = (function () {
            canvas.width = image.width;
            canvas.height = image.height;
            ctx.drawImage(image, 0, 0);
        });
    });
    fileReader.readAsDataURL(obj.files[0]);
}
function messageBox(){
    let elements = []

    elements.push(document.querySelector("#message-container"))
    elements.push(document.querySelector("#error-container"))

    elements.forEach(e => {
        text = e.innerText
        if(text.trim() != "") e.style.display = "block";
        else e.style.display = "none";
    });
}

window.onload = () => {
    messageBox()
}