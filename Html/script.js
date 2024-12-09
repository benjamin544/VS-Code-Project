function showAlert() {
    alert('Hello! Welcome to my website!');
}

function changeBackgroundColor() {
    // בוחר צבע אקראי
    const colors = ['#FF5733', '#33FF57', '#3357FF', '#F0E68C', '#FF69B4'];
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    
    // משנה את צבע הרקע של הדף
    document.body.style.backgroundColor = randomColor;
}


