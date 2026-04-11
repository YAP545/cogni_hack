// --- REPLACE YOUR startExtraction() FUNCTION WITH THIS ---
async function startExtraction() {
  const panel = document.getElementById('extractionPanel');
  const dataPanel = document.getElementById('extractedDataPanel');
  panel.style.display = 'block';
  dataPanel.style.display = 'none';

  const bar = document.getElementById('extBar');
  const pct = document.getElementById('extPct');
  const status = document.getElementById('extStatus');
  const stepEls = document.querySelectorAll('.ext-step');

  // Start fake visual progress for UI feel
  let progress = 0;
  const interval = setInterval(() => {
    progress += Math.random() * 5;
    if (progress > 90) progress = 90; // Hold at 90% until API responds
    bar.style.width = progress + '%';
    pct.textContent = Math.round(progress) + '%';
  }, 150);

  try {
    // Get the actual file the user uploaded
    const file = uploadedFiles[0]; 
    const formData = new FormData();
    formData.append("file", file);

    // Call your FastAPI Backend
    status.textContent = "🧠 AI is reading document...";
    const response = await fetch("http://localhost:8000/api/v1/extract-documents", {
      method: "POST",
      body: formData
    });
    const data = await response.json();
    
    // API finished! Jump to 100%
    clearInterval(interval);
    bar.style.width = '100%';
    pct.textContent = '100%';
    onExtractionDone(data.extracted_data);

  } catch (error) {
    clearInterval(interval);
    status.textContent = "❌ Error connecting to AI API.";
    console.error("API Error:", error);
  }
}

function onExtractionDone(extractedData) {
  document.getElementById('extStatus').textContent = '✅ Extraction complete! Review below.';
  document.querySelectorAll('.ext-step').forEach(s => { s.classList.remove('active'); s.classList.add('done'); });
  setTimeout(() => { document.getElementById('extractedDataPanel').style.display = 'block'; }, 500);
}


// --- GLOBAL VARIABLES TO HOLD API RESULTS ---
let finalRiskScore = 40;
let finalPremium = 248;

// --- REPLACE YOUR initProcessing() FUNCTION WITH THIS ---
async function initProcessing() {
  // Activate first node
  document.getElementById('pn-docs').classList.add('active');
  document.getElementById('procLog').innerHTML = '<div class="log-entry active"><div class="log-dot"></div><div class="log-msg">Connecting to AI Engine...</div></div>';
  
  try {
    // Send the answers from the chat to the backend
    const response = await fetch("http://localhost:8000/api/v1/predict-risk", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        bmi: parseFloat(chatState.answers.bmi) || 24,
        smoking: chatState.answers.smoking || "non-smoker",
        alcohol: chatState.answers.alcohol || "none",
        activity: chatState.answers.activity || "moderate",
        insuranceType: chatState.answers.insuranceType || "term",
        coverage: parseInt(chatState.answers.coverage) || 500
      })
    });
    
    const data = await response.json();
    
    // Save API data to global variables for the Results screen
    finalRiskScore = data.risk_score;
    finalPremium = data.premium_estimate;

    // Transition to Results screen
    document.getElementById('pn-policy').classList.add('done');
    navigateTo('screen-results');

  } catch (error) {
    console.error("Processing API Error:", error);
    document.getElementById('procLog').innerHTML += '<div class="log-entry active"><div class="log-dot" style="background:red;"></div><div class="log-msg" style="color:red;">Error calculating risk. Is backend running?</div></div>';
  }
}
