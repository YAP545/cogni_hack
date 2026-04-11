// Inside your app.js
async function startExtraction(file) {
    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("http://localhost:8000/api/v1/extract-documents", {
            method: "POST",
            body: formData
        });
        const data = await response.json();
        
        // Populate your UI with the real extracted data here
        console.log("AI Extracted Data:", data.extracted_data);
        onExtractionDone(); 
    } catch (error) {
        console.error("Extraction failed:", error);
    }
}
