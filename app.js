/* ============================================================
   app.js — SureScore AI Underwriting Co-Pilot
   ============================================================ */

// ── Particle Canvas ────────────────────────────────────────────
(function initParticles() {
  const canvas = document.getElementById('particleCanvas');
  const ctx = canvas.getContext('2d');
  let W, H, particles = [], animId;

  function resize() {
    W = canvas.width = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }

  class Particle {
    constructor() { this.reset(); }
    reset() {
      this.x = Math.random() * W;
      this.y = Math.random() * H;
      this.r = Math.random() * 1.5 + 0.5;
      this.vx = (Math.random() - 0.5) * 0.3;
      this.vy = (Math.random() - 0.5) * 0.3;
      this.alpha = Math.random() * 0.5 + 0.1;
      this.color = Math.random() > 0.5 ? '#7C3AED' : '#06B6D4';
    }
    update() {
      this.x += this.vx; this.y += this.vy;
      if (this.x < 0 || this.x > W || this.y < 0 || this.y > H) this.reset();
    }
    draw() {
      ctx.save();
      ctx.globalAlpha = this.alpha;
      ctx.fillStyle = this.color;
      ctx.shadowBlur = 8; ctx.shadowColor = this.color;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    }
  }

  function init() {
    resize();
    particles = Array.from({ length: 120 }, () => new Particle());
    animate();
  }

  function drawConnections() {
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 120) {
          ctx.save();
          ctx.globalAlpha = (1 - dist / 120) * 0.12;
          ctx.strokeStyle = '#7C3AED';
          ctx.lineWidth = 0.5;
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.stroke();
          ctx.restore();
        }
      }
    }
  }

  function animate() {
    animId = requestAnimationFrame(animate);
    ctx.clearRect(0, 0, W, H);
    particles.forEach(p => { p.update(); p.draw(); });
    drawConnections();
  }

  window.addEventListener('resize', resize);
  window.addEventListener('load', init);
})();

// ── Navigation ─────────────────────────────────────────────────
function navigateTo(targetId) {
  const screens = document.querySelectorAll('.screen');
  screens.forEach(s => {
    s.classList.remove('active', 'entering');
    s.style.display = 'none';
  });
  const target = document.getElementById(targetId);
  if (!target) return;
  target.style.display = 'block';
  void target.offsetWidth; // reflow
  target.classList.add('entering');
  setTimeout(() => target.classList.add('active'), 10);

  // Screen-specific init
  if (targetId === 'screen-chat') initChat();
  if (targetId === 'screen-processing') initProcessing();
  if (targetId === 'screen-results') initResults();
  if (targetId === 'screen-upload') initUpload();

  window.scrollTo(0, 0);
}

// ── Landing: Stat counters & typing effect ─────────────────────
function animateCounters() {
  document.querySelectorAll('.stat-num[data-count]').forEach(el => {
    const target = parseFloat(el.dataset.count);
    const suffix = el.nextSibling?.textContent?.trim() || '';
    const duration = 1800;
    const start = performance.now();
    function step(now) {
      const t = Math.min((now - start) / duration, 1);
      const ease = 1 - Math.pow(1 - t, 3);
      el.textContent = Math.round(ease * target);
      if (t < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  });
}

const typingMessages = [
  "Analyzing medical history...",
  "Evaluating lifestyle factors...",
  "Computing risk score...",
  "Generating policy options...",
  "Verifying document data...",
];
let typingIdx = 0;
function cycleTyping() {
  const el = document.getElementById('typingText');
  if (!el) return;
  el.style.opacity = '0';
  setTimeout(() => {
    typingIdx = (typingIdx + 1) % typingMessages.length;
    el.textContent = typingMessages[typingIdx];
    el.style.transition = 'opacity 0.4s';
    el.style.opacity = '1';
  }, 300);
}
setInterval(cycleTyping, 2500);
window.addEventListener('load', () => { setTimeout(animateCounters, 400); });

function startAssessment() {
  const btn = document.getElementById('startBtn');
  btn.innerHTML = '<span class="btn-glow"></span>⏳ Initializing AI...';
  btn.disabled = true;
  setTimeout(() => navigateTo('screen-chat'), 800);
}

// ── Chat Assessment ────────────────────────────────────────────
const chatFlow = [
  {
    step: 0,
    category: 'Personal Info',
    question: "Hello! I'm your AI Underwriting Co-Pilot 🤖\n\nLet's start with your **full name**. This helps personalize your assessment.",
    inputType: 'text',
    placeholder: 'e.g. Alex Johnson',
    key: 'fullName',
    tip: "Your name helps us personalize your policy documents."
  },
  {
    step: 0,
    category: 'Personal Info',
    question: "Great! Now, what's your **date of birth**? We'll automatically calculate your age for risk assessment.",
    inputType: 'text',
    placeholder: 'DD / MM / YYYY',
    key: 'dob',
    tip: "Age is one of the most significant risk factors in insurance underwriting."
  },
  {
    step: 0,
    category: 'Personal Info',
    question: "What is your **biological sex**? This helps calibrate health risk models.",
    inputType: 'options',
    options: [
      { icon: '👨', label: 'Male', desc: 'Biological male', value: 'male' },
      { icon: '👩', label: 'Female', desc: 'Biological female', value: 'female' },
      { icon: '⚧', label: 'Other', desc: 'Prefer not to say', value: 'other' },
    ],
    key: 'sex',
    tip: "Biological sex influences certain health risk probabilities."
  },
  {
    step: 1,
    category: 'Health Profile',
    question: "Now let's talk about your **health**. Do you have any pre-existing medical conditions?",
    inputType: 'options',
    options: [
      { icon: '✅', label: 'None', desc: 'No known conditions', value: 'none' },
      { icon: '💊', label: 'Managed', desc: 'Controlled with medication', value: 'managed' },
      { icon: '🏥', label: 'Active', desc: 'Ongoing treatment', value: 'active' },
    ],
    key: 'conditions',
    tip: "Pre-existing conditions are handled confidentially and may affect premiums."
  },
  {
    step: 1,
    category: 'Health Profile',
    question: "What is your approximate **BMI** (Body Mass Index)? Use slider to select.",
    inputType: 'slider',
    min: 14, max: 45, default: 24,
    unit: 'kg/m²',
    key: 'bmi',
    tip: "BMI between 18.5–24.9 is considered healthy and gets the best premium rates."
  },
  {
    step: 2,
    category: 'Lifestyle',
    question: "Do you **smoke** or use tobacco products?",
    inputType: 'options',
    options: [
      { icon: '🚭', label: 'Non-Smoker', desc: 'Never or quit >5 yrs', value: 'non-smoker' },
      { icon: '🚬', label: 'Ex-Smoker', desc: 'Quit within 5 years', value: 'ex-smoker' },
      { icon: '😮‍💨', label: 'Smoker', desc: 'Current tobacco user', value: 'smoker' },
    ],
    key: 'smoking',
    tip: "Smoking adds 30–40% to insurance premiums due to significant health risks."
  },
  {
    step: 2,
    category: 'Lifestyle',
    question: "How would you describe your **alcohol consumption**?",
    inputType: 'options',
    options: [
      { icon: '💧', label: 'None', desc: 'No alcohol', value: 'none' },
      { icon: '🍷', label: 'Moderate', desc: '1-2 drinks/day', value: 'moderate' },
      { icon: '🍺', label: 'Heavy', desc: '3+ drinks/day', value: 'heavy' },
    ],
    key: 'alcohol',
    tip: "Heavy alcohol use increases risk of liver disease, accidents, and cardiovascular issues."
  },
  {
    step: 2,
    category: 'Lifestyle',
    question: "How **physically active** are you on average?",
    inputType: 'options',
    options: [
      { icon: '🧘', label: 'Sedentary', desc: 'Little to no exercise', value: 'sedentary' },
      { icon: '🚶', label: 'Moderate', desc: '2-3 sessions/week', value: 'moderate' },
      { icon: '🏃', label: 'Active', desc: '4+ sessions/week', value: 'active' },
      { icon: '🏋️', label: 'Athlete', desc: 'Professional level', value: 'athlete' },
    ],
    key: 'activity',
    tip: "Regular exercise can reduce your premium by up to 15%."
  },
  {
    step: 3,
    category: 'Coverage Needs',
    question: "What **type of insurance** are you looking for?",
    inputType: 'options',
    options: [
      { icon: '🛡️', label: 'Term Life', desc: 'Fixed coverage period', value: 'term' },
      { icon: '💎', label: 'Whole Life', desc: 'Lifetime coverage', value: 'whole' },
      { icon: '❤️', label: 'Health', desc: 'Medical coverage', value: 'health' },
      { icon: '🏠', label: 'Home', desc: 'Property protection', value: 'home' },
    ],
    key: 'insuranceType',
    tip: "Term Life is the most cost-effective for most applicants under 45."
  },
  {
    step: 3,
    category: 'Coverage Needs',
    question: "What **coverage amount** would you like? (in $1000s)",
    inputType: 'slider',
    min: 50, max: 2000, default: 500,
    unit: 'K coverage',
    key: 'coverage',
    tip: "Common rule: coverage = 10–15× your annual income."
  },
];

let chatState = {
  qIndex: 0,
  answers: {},
  currentStep: 0,
};

function initChat() {
  chatState = { qIndex: 0, answers: {}, currentStep: 0 };
  document.getElementById('chatMessages').innerHTML = '';
  updateSidebarProgress(0);
  setTimeout(() => askQuestion(0), 400);
}

function askQuestion(idx) {
  if (idx >= chatFlow.length) {
    finishChat();
    return;
  }
  const q = chatFlow[idx];
  chatState.currentStep = q.step;
  updateSidebarProgress(idx);
  updateAiTip(q.tip);
  addAiMessage(q.question);
  setTimeout(() => renderInput(q), 800);
}

function addAiMessage(text) {
  const wrap = document.createElement('div');
  wrap.className = 'msg-wrap msg-ai';
  // Convert **bold** markdown
  const html = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>').replace(/\n/g, '<br/>');
  wrap.innerHTML = `
    <div class="typing-indicator" id="typing-ind">
      <div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>
    </div>`;
  const msgs = document.getElementById('chatMessages');
  msgs.appendChild(wrap);
  msgs.scrollTop = msgs.scrollHeight;

  setTimeout(() => {
    wrap.innerHTML = `
      <div class="msg-bubble">${html}</div>
      <div class="msg-time">${getTime()}</div>`;
    msgs.scrollTop = msgs.scrollHeight;
  }, 900);
}

function addUserMessage(text) {
  const wrap = document.createElement('div');
  wrap.className = 'msg-wrap msg-user';
  wrap.innerHTML = `
    <div class="msg-bubble">${text}</div>
    <div class="msg-time">${getTime()}</div>`;
  document.getElementById('chatMessages').appendChild(wrap);
  document.getElementById('chatMessages').scrollTop = 9999;
}

function getTime() {
  return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

function renderInput(q) {
  const area = document.getElementById('chatInputArea');
  area.innerHTML = '';

  if (q.inputType === 'options') {
    area.innerHTML = `
      <div class="input-label">Select an option</div>
      <div class="option-cards" id="optionCards">
        ${q.options.map((o, i) => `
          <div class="option-card" data-val="${o.value}" data-label="${o.label}" onclick="selectOption(this, '${q.key}')">
            <span class="opt-icon">${o.icon}</span>
            <div class="opt-label">${o.label}</div>
            <div class="opt-desc">${o.desc}</div>
          </div>`).join('')}
      </div>`;
  } else if (q.inputType === 'text') {
    area.innerHTML = `
      <div class="input-label">Type your answer</div>
      <div class="chat-text-input-wrap">
        <input type="text" class="chat-text-input" id="chatTextInput" placeholder="${q.placeholder}" />
        <button class="btn-primary small" onclick="submitText('${q.key}')">
          <span class="btn-glow"></span>Next →
        </button>
      </div>`;
    const inp = document.getElementById('chatTextInput');
    inp.focus();
    inp.addEventListener('keydown', e => { if (e.key === 'Enter') submitText(q.key); });
  } else if (q.inputType === 'slider') {
    const mid = q.default;
    area.innerHTML = `
      <div class="input-label">Adjust the value</div>
      <div class="slider-wrap">
        <div class="slider-value" id="sliderVal">${mid} ${q.unit}</div>
        <input type="range" class="chat-slider" id="chatSlider" min="${q.min}" max="${q.max}" value="${mid}" oninput="updateSlider(this, '${q.unit}')"/>
        <div class="slider-labels"><span>${q.min}</span><span>${q.max}</span></div>
      </div>
      <button class="nav-next-btn" onclick="submitSlider('${q.key}', '${q.unit}')">
        Confirm ${mid} ${q.unit} →
      </button>`;
    updateSlider(document.getElementById('chatSlider'), q.unit);
  }
}

function selectOption(el, key) {
  document.querySelectorAll('.option-card').forEach(c => c.classList.remove('selected'));
  el.classList.add('selected');
  const val = el.dataset.val;
  const label = el.dataset.label;
  setTimeout(() => {
    chatState.answers[key] = val;
    addUserMessage(el.querySelector('.opt-icon').textContent + ' ' + label);
    document.getElementById('chatInputArea').innerHTML = '';
    chatState.qIndex++;
    setTimeout(() => askQuestion(chatState.qIndex), 700);
  }, 400);
}

function submitText(key) {
  const inp = document.getElementById('chatTextInput');
  const val = inp.value.trim();
  if (!val) { inp.style.borderColor = '#EF4444'; setTimeout(() => inp.style.borderColor = '', 1000); return; }
  chatState.answers[key] = val;
  addUserMessage(val);
  document.getElementById('chatInputArea').innerHTML = '';
  chatState.qIndex++;
  setTimeout(() => askQuestion(chatState.qIndex), 700);
}

function updateSlider(el, unit) {
  const val = el.value;
  document.getElementById('sliderVal').textContent = `${val} ${unit}`;
  // Update gradient fill
  const pct = ((val - el.min) / (el.max - el.min)) * 100;
  el.style.backgroundSize = `${pct}% 100%`;
  // Update confirm button text
  const btn = document.querySelector('.nav-next-btn');
  if (btn) btn.textContent = `Confirm ${val} ${unit} →`;
}

function submitSlider(key, unit) {
  const val = document.getElementById('chatSlider').value;
  chatState.answers[key] = val;
  addUserMessage(`${val} ${unit}`);
  document.getElementById('chatInputArea').innerHTML = '';
  chatState.qIndex++;
  setTimeout(() => askQuestion(chatState.qIndex), 700);
}

function updateSidebarProgress(qIdx) {
  const total = chatFlow.length;
  const pct = Math.round((qIdx / total) * 100);
  document.getElementById('sidebarProgress').style.width = pct + '%';
  document.getElementById('sidebarPct').textContent = pct + '%';

  // Sync mobile progress strip
  const mStrip = document.getElementById('mobileProgressStrip');
  const mFill  = document.getElementById('mobileProgFill');
  const mPct   = document.getElementById('mobilePct');
  const mLabel = document.getElementById('mobileStepLabel');
  if (mStrip) {
    const isMobile = window.innerWidth <= 640;
    mStrip.style.display = isMobile ? 'flex' : 'none';
    if (mFill)  mFill.style.width = pct + '%';
    if (mPct)   mPct.textContent  = pct + '%';
    const stepIcons = ['👤','❤️','🏃','💼','📄'];
    const stepNames = ['Personal Info','Health Profile','Lifestyle','Coverage Needs','Documents'];
    const currentStep = chatFlow[qIdx]?.step ?? 4;
    if (mLabel) mLabel.textContent = (stepIcons[currentStep] || '📋') + ' ' + (stepNames[currentStep] || 'Complete');
  }

  // Update step items
  const currentStep = chatFlow[qIdx]?.step ?? 4;
  document.querySelectorAll('.step-item').forEach((el, i) => {
    el.classList.remove('active', 'completed');
    if (i < currentStep) {
      el.classList.add('completed');
      el.querySelector('.step-status').textContent = 'Done ✓';
    } else if (i === currentStep) {
      el.classList.add('active');
      el.querySelector('.step-status').textContent = 'In Progress';
    } else {
      el.querySelector('.step-status').textContent = 'Pending';
    }
  });
}

function updateAiTip(tip) {
  const el = document.getElementById('aiTip');
  if (el && tip) {
    el.style.opacity = '0';
    setTimeout(() => { el.textContent = tip; el.style.transition = 'opacity 0.4s'; el.style.opacity = '1'; }, 200);
  }
}

function finishChat() {
  addAiMessage("Excellent! 🎉 I have all the information I need.\n\n**Last step:** Please upload your documents for AI-powered data extraction. This takes about 30 seconds!");
  const area = document.getElementById('chatInputArea');
  area.innerHTML = `
    <button class="btn-primary" onclick="navigateTo('screen-upload')" style="margin-top:8px;">
      <span class="btn-glow"></span>
      📄 Upload Documents →
    </button>`;
  updateSidebarProgress(chatFlow.length);

  // Mark step 4 (docs) as active
  document.querySelectorAll('.step-item').forEach((el, i) => {
    el.classList.remove('active', 'completed');
    if (i < 4) { el.classList.add('completed'); el.querySelector('.step-status').textContent = 'Done ✓'; }
    else if (i === 4) { el.classList.add('active'); el.querySelector('.step-status').textContent = 'In Progress'; }
  });
}

// ── Upload Screen ──────────────────────────────────────────────
let uploadedFiles = [];

function initUpload() {
  uploadedFiles = [];
  renderFileList();
  document.getElementById('extractionPanel').style.display = 'none';
  document.getElementById('extractedDataPanel').style.display = 'none';

  // Drag and drop
  const dz = document.getElementById('dropZone');
  if (!dz) return;
  dz.addEventListener('dragover', e => { e.preventDefault(); dz.classList.add('drag-over'); });
  dz.addEventListener('dragleave', () => dz.classList.remove('drag-over'));
  dz.addEventListener('drop', e => {
    e.preventDefault();
    dz.classList.remove('drag-over');
    handleFiles(Array.from(e.dataTransfer.files));
  });
}

function handleFileSelect(e) { handleFiles(Array.from(e.target.files)); }

function handleFiles(files) {
  files.forEach(f => {
    if (!uploadedFiles.find(u => u.name === f.name)) {
      uploadedFiles.push(f);
    }
  });
  renderFileList();
  if (uploadedFiles.length > 0) startExtraction();
}

function getFileIcon(name) {
  const ext = name.split('.').pop().toLowerCase();
  if (ext === 'pdf') return '📄';
  if (['jpg','jpeg','png','gif'].includes(ext)) return '🖼️';
  if (['doc','docx'].includes(ext)) return '📝';
  return '📁';
}

function formatSize(bytes) {
  if (bytes < 1024) return bytes + ' B';
  if (bytes < 1048576) return (bytes/1024).toFixed(1) + ' KB';
  return (bytes/1048576).toFixed(1) + ' MB';
}

function renderFileList() {
  const container = document.getElementById('fileList');
  const count = document.getElementById('fileCount');
  count.textContent = uploadedFiles.length + ' file' + (uploadedFiles.length !== 1 ? 's' : '');
  if (uploadedFiles.length === 0) {
    container.innerHTML = '<div class="no-files">No files uploaded yet</div>';
    return;
  }
  container.innerHTML = uploadedFiles.map((f, i) => `
    <div class="file-item">
      <div class="file-icon">${getFileIcon(f.name)}</div>
      <div class="file-info">
        <div class="file-name">${f.name}</div>
        <div class="file-size-label">${formatSize(f.size)}</div>
      </div>
      <button class="file-remove" onclick="removeFile(${i})">✕</button>
    </div>`).join('');
}

function removeFile(idx) {
  uploadedFiles.splice(idx, 1);
  renderFileList();
  if (uploadedFiles.length === 0) {
    document.getElementById('extractionPanel').style.display = 'none';
    document.getElementById('extractedDataPanel').style.display = 'none';
  }
}

const extractionSteps = [
  "🔍 Detecting document type...",
  "📝 Running OCR text extraction...",
  "🧠 Parsing medical fields...",
  "✅ Validating extracted data...",
];

function startExtraction() {
  const panel = document.getElementById('extractionPanel');
  const dataPanel = document.getElementById('extractedDataPanel');
  panel.style.display = 'block';
  dataPanel.style.display = 'none';

  const bar = document.getElementById('extBar');
  const pct = document.getElementById('extPct');
  const status = document.getElementById('extStatus');
  const stepEls = document.querySelectorAll('.ext-step');

  let progress = 0;
  let stepIdx = 0;

  // Reset steps
  stepEls.forEach(s => s.classList.remove('active', 'done'));

  const interval = setInterval(() => {
    progress += Math.random() * 4 + 1;
    if (progress >= 100) { progress = 100; clearInterval(interval); onExtractionDone(); }
    bar.style.width = progress + '%';
    pct.textContent = Math.round(progress) + '%';

    // Advance steps
    const newStepIdx = Math.floor(progress / 26);
    if (newStepIdx > stepIdx && newStepIdx < extractionSteps.length) {
      stepEls[stepIdx]?.classList.remove('active');
      stepEls[stepIdx]?.classList.add('done');
      stepIdx = newStepIdx;
      stepEls[stepIdx]?.classList.add('active');
      status.textContent = extractionSteps[stepIdx];
    } else if (stepIdx === 0) {
      stepEls[0].classList.add('active');
      status.textContent = extractionSteps[0];
    }
  }, 120);
}

function onExtractionDone() {
  document.getElementById('extStatus').textContent = '✅ Extraction complete! Review and confirm below.';
  document.querySelectorAll('.ext-step').forEach(s => { s.classList.remove('active'); s.classList.add('done'); });
  setTimeout(() => { document.getElementById('extractedDataPanel').style.display = 'block'; }, 500);
}

// ── Processing Screen ──────────────────────────────────────────
const processingLogs = [
  { msg: "Loading AI Underwriting Engine v3.2...", time: "0.1s", node: null, edge: null },
  { msg: "Parsing uploaded documents...", time: "0.3s", node: 'pn-docs', edge: null },
  { msg: "Running OCR pipeline on medical records...", time: "0.6s", node: null, edge: null },
  { msg: "Document extraction complete ✓", time: "0.9s", node: null, edge: 'pe-1' },
  { msg: "Initializing Neural Risk Model (NRM-7)...", time: "1.1s", node: 'pn-extract', edge: null },
  { msg: "Extracting 247 health biomarkers...", time: "1.5s", node: null, edge: null },
  { msg: "Mapping lifestyle patterns → risk vectors...", time: "1.9s", node: null, edge: null },
  { msg: "AI extraction pipeline complete ✓", time: "2.2s", node: null, edge: 'pe-2' },
  { msg: "Activating Risk Scoring Engine...", time: "2.4s", node: 'pn-risk', edge: null },
  { msg: "Calculating actuarial risk score...", time: "2.7s", node: null, edge: null },
  { msg: "Running Monte Carlo simulations (10K iterations)...", time: "2.9s", node: null, edge: null },
  { msg: "Risk profile finalized: Score 40/100 (Low Risk) ✓", time: "3.1s", node: null, edge: 'pe-3' },
  { msg: "Generating personalized policy terms...", time: "3.3s", node: 'pn-policy', edge: null },
  { msg: "Premium calculation complete: $248/mo ✓", time: "3.5s", node: null, edge: null },
  { msg: "🎉 Assessment complete! Generating your dashboard...", time: "3.7s", node: null, edge: null },
];

function initProcessing() {
  // Reset pipeline
  ['pn-docs','pn-extract','pn-risk','pn-policy'].forEach(id => {
    const el = document.getElementById(id);
    if (el) { el.className = 'pipeline-node'; el.querySelector('.pn-status').textContent = 'Queued'; }
  });
  ['pe-1','pe-2','pe-3'].forEach(id => {
    const el = document.getElementById(id);
    if (el) { el.classList.remove('active'); el.querySelector('.edge-fill').style.width = '0%'; }
  });

  document.getElementById('procLog').innerHTML = '';
  document.getElementById('factorsVal').textContent = '0';
  document.getElementById('confVal').textContent = '0%';
  document.getElementById('timeVal').textContent = '0.0s';

  // Activate first node
  document.getElementById('pn-docs').classList.add('active');
  document.getElementById('pn-docs').querySelector('.pn-status').textContent = 'Processing';

  let logIdx = 0;
  let factors = 0;
  let conf = 0;
  let startTime = Date.now();

  function addLog(entry) {
    if (logIdx > 0) {
      // Mark previous as done
      const prev = document.getElementById('log-' + (logIdx - 1));
      if (prev) { prev.classList.remove('active'); prev.classList.add('done'); prev.querySelector('.log-dot').style.animationPlayState = 'paused'; }
    }
    const el = document.createElement('div');
    el.className = 'log-entry active';
    el.id = 'log-' + logIdx;
    el.innerHTML = `<div class="log-dot"></div><div class="log-msg">${entry.msg}</div><div class="log-time">${entry.time}</div>`;
    document.getElementById('procLog').appendChild(el);
    document.getElementById('procLog').scrollTop = 9999;

    // Pipeline node/edge activation
    if (entry.node) {
      const node = document.getElementById(entry.node);
      if (node) { node.classList.add('active'); node.querySelector('.pn-status').textContent = 'Processing'; }
    }
    if (entry.edge) {
      const edge = document.getElementById(entry.edge);
      if (edge) { edge.classList.add('active'); }
      // Mark previous node done
      const nodes = ['pn-docs','pn-extract','pn-risk','pn-policy'];
      const edgeMap = { 'pe-1': 0, 'pe-2': 1, 'pe-3': 2 };
      const nodeIdx = edgeMap[entry.edge];
      if (nodeIdx !== undefined) {
        const node = document.getElementById(nodes[nodeIdx]);
        if (node) {
          node.classList.remove('active');
          node.classList.add('done');
          node.querySelector('.pn-status').textContent = 'Done ✓';
        }
      }
    }
    logIdx++;
  }

  // Schedule logs
  processingLogs.forEach((entry, i) => {
    setTimeout(() => addLog(entry), i * 240);
  });

  // Animate metrics
  const metricsInterval = setInterval(() => {
    factors = Math.min(247, factors + Math.floor(Math.random() * 15));
    conf = Math.min(94, conf + Math.floor(Math.random() * 5));
    const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
    document.getElementById('factorsVal').textContent = factors;
    document.getElementById('confVal').textContent = conf + '%';
    document.getElementById('timeVal').textContent = elapsed + 's';
  }, 200);

  // Final — mark last node done then navigate
  const totalDuration = processingLogs.length * 240 + 800;
  setTimeout(() => {
    clearInterval(metricsInterval);
    document.getElementById('factorsVal').textContent = '247';
    document.getElementById('confVal').textContent = '94%';
    document.getElementById('timeVal').textContent = '3.7s';
    // Mark policy node done
    const policyNode = document.getElementById('pn-policy');
    if (policyNode) { policyNode.classList.remove('active'); policyNode.classList.add('done'); policyNode.querySelector('.pn-status').textContent = 'Done ✓'; }
    setTimeout(() => navigateTo('screen-results'), 900);
  }, totalDuration);
}

// ── Results Dashboard ──────────────────────────────────────────
function initResults() {
  setTimeout(drawGauge, 300);
  setTimeout(animateExplainBars, 600);
  setTimeout(animateResultCounters, 400);
  setTimeout(animatePremium, 500);
}

function drawGauge() {
  const canvas = document.getElementById('gaugeCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const cx = 140, cy = 140, R = 110;
  const score = 40; // Low risk score
  const targetAngle = Math.PI + (score / 100) * Math.PI;

  let angle = Math.PI;
  const gradient = ctx.createLinearGradient(30, 0, 250, 0);
  gradient.addColorStop(0, '#10B981');
  gradient.addColorStop(0.5, '#F59E0B');
  gradient.addColorStop(1, '#EF4444');

  function draw(currentAngle) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Background arc
    ctx.beginPath();
    ctx.arc(cx, cy, R, Math.PI, 2 * Math.PI);
    ctx.strokeStyle = 'rgba(255,255,255,0.07)';
    ctx.lineWidth = 18;
    ctx.lineCap = 'round';
    ctx.stroke();

    // Colored arc
    ctx.beginPath();
    ctx.arc(cx, cy, R, Math.PI, currentAngle);
    ctx.strokeStyle = gradient;
    ctx.lineWidth = 18;
    ctx.lineCap = 'round';
    ctx.shadowBlur = 20;
    ctx.shadowColor = '#10B981';
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Tick lines
    for (let i = 0; i <= 10; i++) {
      const tickAngle = Math.PI + (i / 10) * Math.PI;
      const x1 = cx + (R - 14) * Math.cos(tickAngle);
      const y1 = cy + (R - 14) * Math.sin(tickAngle);
      const x2 = cx + (R + 4) * Math.cos(tickAngle);
      const y2 = cy + (R + 4) * Math.sin(tickAngle);
      ctx.beginPath();
      ctx.moveTo(x1, y1); ctx.lineTo(x2, y2);
      ctx.strokeStyle = 'rgba(255,255,255,0.12)';
      ctx.lineWidth = 1.5;
      ctx.stroke();
    }

    // Needle
    const nLen = R - 20;
    const nx = cx + nLen * Math.cos(currentAngle);
    const ny = cy + nLen * Math.sin(currentAngle);
    ctx.beginPath();
    ctx.moveTo(cx, cy); ctx.lineTo(nx, ny);
    ctx.strokeStyle = 'white';
    ctx.lineWidth = 3;
    ctx.lineCap = 'round';
    ctx.shadowBlur = 12; ctx.shadowColor = 'rgba(255,255,255,0.8)';
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Center dot
    ctx.beginPath();
    ctx.arc(cx, cy, 8, 0, Math.PI * 2);
    ctx.fillStyle = 'white';
    ctx.shadowBlur = 16; ctx.shadowColor = 'rgba(255,255,255,0.6)';
    ctx.fill(); ctx.shadowBlur = 0;
  }

  // Animate needle + counter
  const startTime = performance.now();
  const duration = 2000;
  let numEl = document.getElementById('gaugeNum');
  let badgeEl = document.getElementById('riskLevelBadge');
  let riskText = document.getElementById('riskLevelText');

  function animate(now) {
    const t = Math.min((now - startTime) / duration, 1);
    const ease = 1 - Math.pow(1 - t, 3);
    const currentAngle = Math.PI + ease * (targetAngle - Math.PI);
    draw(currentAngle);
    if (numEl) numEl.textContent = Math.round(ease * score);
    if (t < 1) requestAnimationFrame(animate);
    else {
      badgeEl.className = 'risk-level-badge low';
      riskText.textContent = '🟢 LOW RISK';
    }
  }
  requestAnimationFrame(animate);
}

function animateExplainBars() {
  document.querySelectorAll('.exp-bar[data-width]').forEach(bar => {
    const w = bar.dataset.width;
    setTimeout(() => { bar.style.width = w + '%'; }, 200);
  });
}

function animateResultCounters() {
  document.querySelectorAll('.ss-val[data-count]').forEach(el => {
    const target = parseFloat(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    const duration = 1800;
    const start = performance.now();
    function step(now) {
      const t = Math.min((now - start) / duration, 1);
      const ease = 1 - Math.pow(1 - t, 3);
      const val = ease * target;
      el.textContent = (target % 1 !== 0 ? val.toFixed(1) : Math.round(val)) + suffix;
      if (t < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  });

  // Score circle
  setTimeout(() => {
    document.getElementById('scoreCircle').style.strokeDashoffset = '158';
  }, 100);
}

function animatePremium() {
  const el = document.getElementById('premiumVal');
  if (!el) return;
  let val = 0;
  const target = 248;
  const interval = setInterval(() => {
    val += 7;
    if (val >= target) { val = target; clearInterval(interval); }
    el.textContent = '$' + val + '/mo';
  }, 30);
}

// ── Window load ────────────────────────────────────────────────
window.addEventListener('load', () => {
  // Ensure landing screen is visible
  const landing = document.getElementById('screen-landing');
  if (landing) landing.style.display = 'block';
});
