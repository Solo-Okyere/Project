function generateQRCode() {
    const qrContainer = document.getElementById('qr-container');
    qrContainer.innerHTML = "";

    // Link to your hosted Valentine page
    const qrText = "https://https://favorite-assets--okyeresolomon.replit.app/"; 

    QRCode.toCanvas(qrContainer, qrText, { 
        width: 120,
        margin: 2,
        color: {
            dark: "#ff4d6d",
            light: "#05070a"
        }
    }, function (error) {
        if (error) console.error(error);
    });
}
