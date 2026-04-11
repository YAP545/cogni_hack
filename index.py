<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"/>
  <meta name="theme-color" content="#030712"/>
  <meta name="mobile-web-app-capable" content="yes"/>
  <meta name="apple-mobile-web-app-capable" content="yes"/>
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"/>
  <title>SureScore – AI Underwriting Co-Pilot</title>
  <meta name="description" content="SureScore AI Underwriting Co-Pilot – From application to policy in minutes. AI-powered insurance underwriting with intelligent risk assessment."/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="style.css"/>
</head>
<body>
  <!-- Animated Background -->
  <div class="bg-canvas">
    <canvas id="particleCanvas"></canvas>
    <div class="grid-overlay"></div>
    <div class="noise-overlay"></div>
  </div>

  <!-- App Shell -->
  <div id="app">

    <!-- ===== SCREEN 1: LANDING ===== -->
    <section class="screen active" id="screen-landing">
      <nav class="navbar">
        <div class="logo">
          <div class="logo-icon">
            <svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="14" stroke="url(#lg1)" stroke-width="2"/><path d="M10 16l4 4 8-8" stroke="url(#lg2)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/><defs><linearGradient id="lg1" x1="0" y1="0" x2="32" y2="32"><stop stop-color="#7C3AED"/><stop offset="1" stop-color="#06B6D4"/></linearGradient><linearGradient id="lg2" x1="0" y1="0" x2="32" y2="32"><stop stop-color="#A78BFA"/><stop offset="1" stop-color="#22D3EE"/></linearGradient></defs></svg>
          </div>
          <span class="logo-text">SureScore</span>
        </div>
        <div class="nav-links">
          <span class="nav-badge">AI-Powered</span>
          <button class="btn-ghost" onclick="navigateTo('screen-chat')">Try Demo</button>
        </div>
      </nav>

      <div class="landing-hero">
        <div class="hero-left">
          <div class="hero-eyebrow">
            <span class="pulse-dot"></span>
            <span>AI Engine Active</span>
          </div>
          <h1 class="hero-title">
            <span class="gradient-text">SureScore</span><br/>
            AI Underwriting<br/>
            <span class="gradient-text-2">Co-Pilot</span>
          </h1>
          <p class="hero-subtitle">From application to policy in minutes.<br/>Intelligent risk assessment powered by advanced AI.</p>

          <div class="hero-stats">
            <div class="stat-item">
              <span class="stat-num" data-count="98">0</span><span>%</span>
              <span class="stat-label">Accuracy</span>
            </div>
            <div class="stat-divider"></div>
            <div class="stat-item">
              <span class="stat-num" data-count="3">0</span><span>min</span>
              <span class="stat-label">Avg. Time</span>
            </div>
            <div class="stat-divider"></div>
            <div class="stat-item">
              <span class="stat-num" data-count="50">0</span><span>K+</span>
              <span class="stat-label">Policies</span>
            </div>
          </div>

          <div class="hero-actions">
            <button class="btn-primary" id="startBtn" onclick="startAssessment()">
              <span class="btn-glow"></span>
              <svg viewBox="0 0 24 24" fill="none" width="20" height="20"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
              Start Smart Assessment
            </button>
            <button class="btn-ghost-2">
              <svg viewBox="0 0 24 24" fill="none" width="18" height="18"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/><path d="M10 8l6 4-6 4V8z" fill="currentColor"/></svg>
              Watch Demo
            </button>
          </div>
        </div>

        <div class="hero-right">
          <div class="floating-ui">
            <div class="float-card card-1">
              <div class="fc-icon">🧠</div>
              <div class="fc-content">
                <div class="fc-title">AI Analysis</div>
                <div class="fc-bar"><div class="fc-fill" style="width:87%"></div></div>
                <div class="fc-val">87% Complete</div>
              </div>
            </div>
            <div class="float-card card-2">
              <div class="fc-icon">🛡️</div>
              <div class="fc-content">
                <div class="fc-title">Risk Score</div>
                <div class="risk-badge low">LOW RISK</div>
                <div class="fc-val">Score: 24/100</div>
              </div>
            </div>
            <div class="float-card card-3">
              <div class="fc-icon">⚡</div>
              <div class="fc-content">
                <div class="fc-title">Processing</div>
                <div class="typing-anim">
                  <span class="typing-text" id="typingText">Analyzing medical history...</span>
                </div>
              </div>
            </div>
            <div class="float-card card-4">
              <div class="fc-icon">💎</div>
              <div class="fc-content">
                <div class="fc-title">Premium</div>
                <div class="fc-price">$248<span>/mo</span></div>
                <div class="fc-sub">Optimal rate found</div>
              </div>
            </div>
            <!-- Central orb -->
            <div class="center-orb">
              <div class="orb-inner">
                <div class="orb-rings">
                  <div class="ring ring-1"></div>
                  <div class="ring ring-2"></div>
                  <div class="ring ring-3"></div>
                </div>
                <svg viewBox="0 0 64 64" width="40" height="40"><path d="M32 8C18.7 8 8 18.7 8 32s10.7 24 24 24 24-10.7 24-24S45.3 8 32 8zm0 44C20.9 52 12 43.1 12 32S20.9 12 32 12s20 8.9 20 20-8.9 20-20 20z" fill="url(#orb-lg)"/><path d="M32 20c-6.6 0-12 5.4-12 12s5.4 12 12 12 12-5.4 12-12-5.4-12-12-12z" fill="url(#orb-lg2)"/><defs><linearGradient id="orb-lg" x1="8" y1="8" x2="56" y2="56"><stop stop-color="#7C3AED"/><stop offset="1" stop-color="#06B6D4"/></linearGradient><linearGradient id="orb-lg2" x1="20" y1="20" x2="44" y2="44"><stop stop-color="#A78BFA"/><stop offset="1" stop-color="#22D3EE"/></linearGradient></defs></svg>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Feature strips -->
      <div class="features-strip">
        <div class="feature-item">
          <svg viewBox="0 0 24 24" fill="none" width="20" height="20"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="url(#fi1)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><defs><linearGradient id="fi1"><stop stop-color="#7C3AED"/><stop offset="1" stop-color="#06B6D4"/></linearGradient></defs></svg>
          <span>Conversational AI Flow</span>
        </div>
        <div class="feature-item">
          <svg viewBox="0 0 24 24" fill="none" width="20" height="20"><path d="M9 12l2 2 4-4" stroke="url(#fi2)" stroke-width="2" stroke-linecap="round"/><rect x="3" y="3" width="18" height="18" rx="3" stroke="url(#fi2)" stroke-width="2"/><defs><linearGradient id="fi2"><stop stop-color="#7C3AED"/><stop offset="1" stop-color="#06B6D4"/></linearGradient></defs></svg>
          <span>Smart Document Extraction</span>
        </div>
        <div class="feature-item">
          <svg viewBox="0 0 24 24" fill="none" width="20" height="20"><circle cx="12" cy="12" r="10" stroke="url(#fi3)" stroke-width="2"/><path d="M12 6v6l4 2" stroke="url(#fi3)" stroke-width="2" stroke-linecap="round"/><defs><linearGradient id="fi3"><stop stop-color="#7C3AED"/><stop offset="1" stop-color="#06B6D4"/></linearGradient></defs></svg>
          <span>Real-time Risk Engine</span>
        </div>
        <div class="feature-item">
          <svg viewBox="0 0 24 24" fill="none" width="20" height="20"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" stroke="url(#fi4)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><defs><linearGradient id="fi4"><stop stop-color="#7C3AED"/><stop offset="1" stop-color="#06B6D4"/></linearGradient></defs></svg>
          <span>AI Explainability Panel</span>
        </div>
      </div>
    </section>

    <!-- ===== SCREEN 2: CHAT ASSESSMENT ===== -->
    <section class="screen" id="screen-chat">
      <div class="chat-layout">
        <!-- Sidebar -->
        <aside class="chat-sidebar">
          <div class="sidebar-logo">
            <div class="logo-icon small">
              <svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="14" stroke="url(#slg1)" stroke-width="2"/><path d="M10 16l4 4 8-8" stroke="url(#slg2)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/><defs><linearGradient id="slg1" x1="0" y1="0" x2="32" y2="32"><stop stop-color="#7C3AED"/><stop offset="1" stop-color="#06B6D4"/></linearGradient><linearGradient id="slg2" x1="0" y1="0" x2="32" y2="32"><stop stop-color="#A78BFA"/><stop offset="1" stop-color="#22D3EE"/></linearGradient></defs></svg>
            </div>
            <span>SureScore</span>
          </div>

          <div class="progress-section">
            <div class="prog-label">Assessment Progress</div>
            <div class="prog-track">
              <div class="prog-fill" id="sidebarProgress" style="width:0%"></div>
            </div>
            <div class="prog-pct" id="sidebarPct">0%</div>
          </div>

          <div class="step-list" id="stepList">
            <div class="step-item active" data-step="0">
              <div class="step-icon">👤</div>
              <div class="step-info">
                <div class="step-name">Personal Info</div>
                <div class="step-status">In Progress</div>
              </div>
              <div class="step-check"></div>
            </div>
            <div class="step-item" data-step="1">
              <div class="step-icon">❤️</div>
              <div class="step-info">
                <div class="step-name">Health Profile</div>
                <div class="step-status">Pending</div>
              </div>
              <div class="step-check"></div>
            </div>
            <div class="step-item" data-step="2">
              <div class="step-icon">🏃</div>
              <div class="step-info">
                <div class="step-name">Lifestyle</div>
                <div class="step-status">Pending</div>
              </div>
              <div class="step-check"></div>
            </div>
            <div class="step-item" data-step="3">
              <div class="step-icon">💼</div>
              <div class="step-info">
                <div class="step-name">Coverage Needs</div>
                <div class="step-status">Pending</div>
              </div>
              <div class="step-check"></div>
            </div>
            <div class="step-item" data-step="4">
              <div class="step-icon">📄</div>
              <div class="step-info">
                <div class="step-name">Documents</div>
                <div class="step-status">Pending</div>
              </div>
              <div class="step-check"></div>
            </div>
          </div>

          <div class="ai-tip-box">
            <div class="tip-header">🤖 AI Tip</div>
            <div class="tip-text" id="aiTip">Your answers help our AI provide the most accurate premium quote. All data is encrypted.</div>
          </div>
        </aside>

        <!-- Chat Main -->
        <main class="chat-main">
          <!-- Mobile-only progress strip (visible when sidebar is hidden) -->
          <div class="mobile-progress-strip" id="mobileProgressStrip" style="display:none">
            <span id="mobileStepLabel">👤 Personal Info</span>
            <div class="mobile-prog-track">
              <div class="mobile-prog-fill" id="mobileProgFill" style="width:0%"></div>
            </div>
            <span id="mobilePct" style="color:var(--cyan-light);font-weight:700">0%</span>
          </div>
          <div class="chat-header">
            <div class="ai-avatar-wrap">
              <div class="ai-avatar">
                <div class="av-ring"></div>
                <span>🤖</span>
              </div>
              <div class="ai-info">
                <div class="ai-name">SureScore AI</div>
                <div class="ai-status"><span class="online-dot"></span>Online · Analyzing your profile</div>
              </div>
            </div>
            <div class="chat-actions">
              <button class="btn-icon" title="Audio"><svg viewBox="0 0 24 24" fill="none" width="18" height="18"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z" stroke="currentColor" stroke-width="2"/><path d="M19 10v2a7 7 0 0 1-14 0v-2M12 19v4M8 23h8" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
              <button class="btn-icon" title="Skip"><svg viewBox="0 0 24 24" fill="none" width="18" height="18"><path d="M5 4l10 8-10 8V4z" fill="currentColor"/><path d="M19 4v16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
            </div>
          </div>

          <div class="chat-messages" id="chatMessages">
            <!-- Messages injected by JS -->
          </div>

          <div class="chat-input-area" id="chatInputArea">
            <!-- Dynamic input injected by JS -->
          </div>
        </main>
      </div>
    </section>

    <!-- ===== SCREEN 3: DOCUMENT UPLOAD ===== -->
    <section class="screen" id="screen-upload">
      <div class="upload-layout">
        <div class="upload-header">
          <button class="back-btn" onclick="navigateTo('screen-chat')">
            <svg viewBox="0 0 24 24" fill="none" width="18" height="18"><path d="M19 12H5M12 5l-7 7 7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            Back
          </button>
          <h2>Document Upload</h2>
          <div class="step-badge">Step 5 of 6</div>
        </div>

        <div class="upload-content">
          <div class="upload-left">
            <div class="upload-intro">
              <div class="section-eyebrow">Smart OCR Extraction</div>
              <h3>Upload Your Documents</h3>
              <p>Our AI extracts and validates data automatically. Upload any medical records, ID proof, or financial documents.</p>
            </div>

            <div class="drop-zone" id="dropZone">
              <div class="drop-glow"></div>
              <input type="file" id="fileInput" multiple accept=".pdf,.jpg,.jpeg,.png,.doc,.docx" style="display:none" onchange="handleFileSelect(event)"/>
              <div class="drop-content" onclick="document.getElementById('fileInput').click()">
                <div class="drop-icon-wrap">
                  <div class="drop-icon-bg"></div>
                  <svg viewBox="0 0 64 64" fill="none" width="48" height="48">
                    <rect x="8" y="8" width="48" height="48" rx="12" stroke="url(#upl1)" stroke-width="2"/>
                    <path d="M32 44V20M22 30l10-10 10 10" stroke="url(#upl2)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
                    <defs>
                      <linearGradient id="upl1" x1="8" y1="8" x2="56" y2="56"><stop stop-color="#7C3AED"/><stop offset="1" stop-color="#06B6D4"/></linearGradient>
                      <linearGradient id="upl2" x1="22" y1="20" x2="42" y2="44"><stop stop-color="#A78BFA"/><stop offset="1" stop-color="#22D3EE"/></linearGradient>
                    </defs>
                  </svg>
                </div>
                <div class="drop-text">
                  <strong>Drag & drop files here</strong>
                  <span>or click to browse</span>
                </div>
                <div class="drop-formats">PDF, JPG, PNG, DOC · Max 10MB per file</div>
              </div>
            </div>

            <div class="doc-types">
              <div class="doc-type-item">
                <span class="doc-icon">🪪</span>
                <div>
                  <div class="doc-name">ID Proof</div>
                  <div class="doc-desc">Passport, Aadhaar, Driver's License</div>
                </div>
                <div class="doc-status required">Required</div>
              </div>
              <div class="doc-type-item">
                <span class="doc-icon">🏥</span>
                <div>
                  <div class="doc-name">Medical Records</div>
                  <div class="doc-desc">Lab reports, prescriptions, history</div>
                </div>
                <div class="doc-status optional">Optional</div>
              </div>
              <div class="doc-type-item">
                <span class="doc-icon">💰</span>
                <div>
                  <div class="doc-name">Income Proof</div>
                  <div class="doc-desc">Salary slips, bank statements</div>
                </div>
                <div class="doc-status required">Required</div>
              </div>
            </div>
          </div>

          <div class="upload-right">
            <div class="file-list-panel">
              <div class="panel-header">
                <span>Uploaded Files</span>
                <span class="file-count" id="fileCount">0 files</span>
              </div>
              <div class="file-list" id="fileList">
                <div class="no-files">No files uploaded yet</div>
              </div>
            </div>

            <div class="extraction-panel" id="extractionPanel" style="display:none;">
              <div class="ext-header">
                <div class="ext-ai-badge">
                  <span class="pulse-dot cyan"></span>
                  AI Scanning
                </div>
                <div class="ext-pct" id="extPct">0%</div>
              </div>
              <div class="ext-bar-wrap">
                <div class="ext-bar" id="extBar" style="width:0%"></div>
              </div>
              <div class="ext-status" id="extStatus">Initializing scanner...</div>
              <div class="ext-steps" id="extSteps">
                <div class="ext-step active">🔍 Document detection</div>
                <div class="ext-step">📝 Text extraction (OCR)</div>
                <div class="ext-step">🧠 Data validation</div>
                <div class="ext-step">✅ Confidence scoring</div>
              </div>
            </div>

            <div class="extracted-data-panel" id="extractedDataPanel" style="display:none;">
              <div class="panel-header">
                <span>Extracted Data</span>
                <button class="btn-edit-all">Edit All</button>
              </div>
              <div class="extracted-table">
                <div class="ext-row">
                  <div class="ext-key">Full Name</div>
                  <div class="ext-val">
                    <input type="text" value="Alex Johnson" class="ext-input"/>
                    <div class="conf-badge high">98%</div>
                  </div>
                </div>
                <div class="ext-row">
                  <div class="ext-key">Date of Birth</div>
                  <div class="ext-val">
                    <input type="text" value="15 Mar 1990" class="ext-input"/>
                    <div class="conf-badge high">97%</div>
                  </div>
                </div>
                <div class="ext-row">
                  <div class="ext-key">Blood Group</div>
                  <div class="ext-val">
                    <input type="text" value="O+" class="ext-input"/>
                    <div class="conf-badge medium">85%</div>
                  </div>
                </div>
                <div class="ext-row">
                  <div class="ext-key">BMI</div>
                  <div class="ext-val">
                    <input type="text" value="23.4" class="ext-input"/>
                    <div class="conf-badge high">92%</div>
                  </div>
                </div>
                <div class="ext-row">
                  <div class="ext-key">Income (Annual)</div>
                  <div class="ext-val">
                    <input type="text" value="$85,000" class="ext-input"/>
                    <div class="conf-badge low">71%</div>
                  </div>
                </div>
              </div>
              <button class="btn-primary full-width" onclick="navigateTo('screen-processing')">
                <span class="btn-glow"></span>
                Confirm & Analyze
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ===== SCREEN 4: AI PROCESSING ===== -->
    <section class="screen" id="screen-processing">
      <div class="processing-layout">
        <div class="proc-header">
          <div class="proc-badge">
            <span class="pulse-dot cyan"></span>
            AI Processing
          </div>
          <h2>Analyzing Your Profile</h2>
          <p>Our AI engine is evaluating 200+ risk factors in real-time</p>
        </div>

        <div class="pipeline">
          <div class="pipeline-node pn-docs active" id="pn-docs">
            <div class="pn-glow"></div>
            <div class="pn-icon">📄</div>
            <div class="pn-label">Documents</div>
            <div class="pn-status">Ready</div>
          </div>
          <div class="pipeline-edge" id="pe-1">
            <div class="edge-fill"></div>
          </div>
          <div class="pipeline-node" id="pn-extract">
            <div class="pn-glow"></div>
            <div class="pn-icon">🧠</div>
            <div class="pn-label">AI Extraction</div>
            <div class="pn-status">Queued</div>
          </div>
          <div class="pipeline-edge" id="pe-2">
            <div class="edge-fill"></div>
          </div>
          <div class="pipeline-node" id="pn-risk">
            <div class="pn-glow"></div>
            <div class="pn-icon">⚙️</div>
            <div class="pn-label">Risk Engine</div>
            <div class="pn-status">Queued</div>
          </div>
          <div class="pipeline-edge" id="pe-3">
            <div class="edge-fill"></div>
          </div>
          <div class="pipeline-node" id="pn-policy">
            <div class="pn-glow"></div>
            <div class="pn-icon">📋</div>
            <div class="pn-label">Policy Generator</div>
            <div class="pn-status">Queued</div>
          </div>
        </div>

        <div class="proc-log" id="procLog">
          <div class="log-entry active" id="log-0">
            <div class="log-dot"></div>
            <div class="log-msg">Initializing AI Underwriting Engine...</div>
            <div class="log-time">0.0s</div>
          </div>
        </div>

        <div class="proc-metrics">
          <div class="metric-card">
            <div class="metric-val" id="factorsVal">0</div>
            <div class="metric-label">Risk Factors Analyzed</div>
          </div>
          <div class="metric-card">
            <div class="metric-val" id="confVal">0%</div>
            <div class="metric-label">Model Confidence</div>
          </div>
          <div class="metric-card">
            <div class="metric-val" id="timeVal">0.0s</div>
            <div class="metric-label">Processing Time</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ===== SCREEN 5: RESULTS DASHBOARD ===== -->
    <section class="screen" id="screen-results">
      <div class="results-layout">
        <!-- Top bar -->
        <header class="results-header">
          <div class="logo small">
            <div class="logo-icon small">
              <svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="14" stroke="url(#rlg1)" stroke-width="2"/><path d="M10 16l4 4 8-8" stroke="url(#rlg2)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/><defs><linearGradient id="rlg1" x1="0" y1="0" x2="32" y2="32"><stop stop-color="#7C3AED"/><stop offset="1" stop-color="#06B6D4"/></linearGradient><linearGradient id="rlg2" x1="0" y1="0" x2="32" y2="32"><stop stop-color="#A78BFA"/><stop offset="1" stop-color="#22D3EE"/></linearGradient></defs></svg>
            </div>
            <span class="logo-text">SureScore</span>
          </div>
          <div class="result-actions">
            <button class="btn-ghost" onclick="navigateTo('screen-landing')">New Assessment</button>
            <button class="btn-primary small">
              <span class="btn-glow"></span>
              Download Report
            </button>
          </div>
        </header>

        <div class="results-grid">
          <!-- Risk Gauge -->
          <div class="glass-card risk-gauge-card">
            <div class="card-header">
              <span class="card-title">Risk Score</span>
              <span class="badge-ai">AI Assessed</span>
            </div>
            <div class="gauge-wrap">
              <canvas id="gaugeCanvas" width="280" height="160"></canvas>
              <div class="gauge-score">
                <div class="gauge-num" id="gaugeNum">0</div>
                <div class="gauge-label">out of 100</div>
              </div>
            </div>
            <div class="risk-level-badge" id="riskLevelBadge">
              <span class="risk-dot"></span>
              <span id="riskLevelText">Calculating...</span>
            </div>
            <div class="gauge-legend">
              <span class="leg-item low">Low</span>
              <span class="leg-item medium">Medium</span>
              <span class="leg-item high">High</span>
            </div>
          </div>

          <!-- Policy Card -->
          <div class="glass-card policy-card">
            <div class="card-header">
              <span class="card-title">Recommended Policy</span>
              <span class="policy-badge">Auto-Generated</span>
            </div>
            <div class="policy-plan">
              <div class="plan-name">SureGuard Premium</div>
              <div class="plan-type">Term Life · 20 Years</div>
            </div>
            <div class="policy-details">
              <div class="policy-row">
                <span>Monthly Premium</span>
                <span class="policy-val premium-val" id="premiumVal">$0/mo</span>
              </div>
              <div class="policy-row">
                <span>Coverage Amount</span>
                <span class="policy-val">$500,000</span>
              </div>
              <div class="policy-row">
                <span>Policy Term</span>
                <span class="policy-val">20 Years</span>
              </div>
              <div class="policy-row">
                <span>AI Confidence</span>
                <span class="policy-val conf-val">94%</span>
              </div>
            </div>
            <button class="btn-primary full-width mt-16">
              <span class="btn-glow"></span>
              Accept Policy
            </button>
            <button class="btn-ghost-2 full-width mt-8">Request Human Review</button>
          </div>

          <!-- AI Explainability -->
          <div class="glass-card explain-card">
            <div class="card-header">
              <span class="card-title">AI Explainability</span>
              <span class="badge-ai">SHAP Analysis</span>
            </div>
            <div class="explain-list" id="explainList">
              <div class="explain-item positive">
                <div class="exp-icon">🚭</div>
                <div class="exp-content">
                  <div class="exp-label">Non-Smoker</div>
                  <div class="exp-bar-wrap">
                    <div class="exp-bar" data-width="72" style="width:0%"></div>
                  </div>
                </div>
                <div class="exp-impact negative">-18% risk</div>
              </div>
              <div class="explain-item negative">
                <div class="exp-icon">⚖️</div>
                <div class="exp-content">
                  <div class="exp-label">BMI: 27.4</div>
                  <div class="exp-bar-wrap">
                    <div class="exp-bar danger" data-width="45" style="width:0%"></div>
                  </div>
                </div>
                <div class="exp-impact positive">+12% risk</div>
              </div>
              <div class="explain-item positive">
                <div class="exp-icon">🏃</div>
                <div class="exp-content">
                  <div class="exp-label">Active Lifestyle</div>
                  <div class="exp-bar-wrap">
                    <div class="exp-bar" data-width="58" style="width:0%"></div>
                  </div>
                </div>
                <div class="exp-impact negative">-9% risk</div>
              </div>
              <div class="explain-item negative">
                <div class="exp-icon">🍷</div>
                <div class="exp-content">
                  <div class="exp-label">Moderate Alcohol</div>
                  <div class="exp-bar-wrap">
                    <div class="exp-bar danger" data-width="30" style="width:0%"></div>
                  </div>
                </div>
                <div class="exp-impact positive">+8% risk</div>
              </div>
              <div class="explain-item positive">
                <div class="exp-icon">🏥</div>
                <div class="exp-content">
                  <div class="exp-label">No Pre-existing Conditions</div>
                  <div class="exp-bar-wrap">
                    <div class="exp-bar" data-width="85" style="width:0%"></div>
                  </div>
                </div>
                <div class="exp-impact negative">-22% risk</div>
              </div>
            </div>
          </div>

          <!-- Gamification / Score Improvement -->
          <div class="glass-card gamify-card">
            <div class="card-header">
              <span class="card-title">Improve Your Score</span>
              <span class="badge-ai">Personalized Tips</span>
            </div>
            <div class="score-circle-wrap">
              <div class="score-circle">
                <svg viewBox="0 0 100 100" width="120" height="120">
                  <circle cx="50" cy="50" r="42" fill="none" stroke="#1e1e3f" stroke-width="10"/>
                  <circle cx="50" cy="50" r="42" fill="none" stroke="url(#sc-grad)" stroke-width="10" stroke-linecap="round" stroke-dasharray="264" stroke-dashoffset="158" id="scoreCircle" style="transition: stroke-dashoffset 2s ease;"/>
                  <defs><linearGradient id="sc-grad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#7C3AED"/><stop offset="100%" stop-color="#06B6D4"/></linearGradient></defs>
                </svg>
                <div class="score-circle-val">
                  <span id="scoreCircleNum">40</span>
                  <span class="score-circle-label">/100</span>
                </div>
              </div>
            </div>
            <div class="tip-list">
              <div class="tip-item" data-points="15">
                <div class="tip-badge">+15 pts</div>
                <div class="tip-content">
                  <div class="tip-title">Improve BMI to healthy range</div>
                  <div class="tip-desc">Get better premium rates</div>
                </div>
                <svg viewBox="0 0 24 24" fill="none" width="16" height="16"><path d="M9 18l6-6-6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
              </div>
              <div class="tip-item" data-points="20">
                <div class="tip-badge">+20 pts</div>
                <div class="tip-content">
                  <div class="tip-title">Reduce alcohol consumption</div>
                  <div class="tip-desc">Significant premium reduction</div>
                </div>
                <svg viewBox="0 0 24 24" fill="none" width="16" height="16"><path d="M9 18l6-6-6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
              </div>
              <div class="tip-item" data-points="10">
                <div class="tip-badge">+10 pts</div>
                <div class="tip-content">
                  <div class="tip-title">Annual health checkup</div>
                  <div class="tip-desc">Adds wellness discount</div>
                </div>
                <svg viewBox="0 0 24 24" fill="none" width="16" height="16"><path d="M9 18l6-6-6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
              </div>
            </div>
            <div class="potential-score">
              <span>Potential Score: </span>
              <span class="pot-val">85/100</span>
              <span class="pot-label">→ Premium savings of ~$42/mo</span>
            </div>
          </div>

          <!-- Badges -->
          <div class="glass-card badges-card">
            <div class="card-header">
              <span class="card-title">Your Badges</span>
            </div>
            <div class="badges-grid">
              <div class="badge-item earned">
                <div class="badge-icon">🚭</div>
                <div class="badge-name">Clean Air</div>
                <div class="badge-desc">Non-smoker</div>
              </div>
              <div class="badge-item earned">
                <div class="badge-icon">💪</div>
                <div class="badge-name">Active Life</div>
                <div class="badge-desc">Regular exercise</div>
              </div>
              <div class="badge-item">
                <div class="badge-icon locked">🔒</div>
                <div class="badge-name">Wellness Pro</div>
                <div class="badge-desc">Annual checkup</div>
              </div>
              <div class="badge-item">
                <div class="badge-icon locked">🔒</div>
                <div class="badge-name">Healthy BMI</div>
                <div class="badge-desc">BMI 18.5-24.9</div>
              </div>
            </div>
          </div>

          <!-- Summary stats -->
          <div class="glass-card stats-card">
            <div class="card-header">
              <span class="card-title">Assessment Summary</span>
            </div>
            <div class="summary-stats">
              <div class="sum-stat">
                <div class="ss-icon">⚡</div>
                <div class="ss-val" data-count="3.2" data-suffix="s">0s</div>
                <div class="ss-label">Processing Time</div>
              </div>
              <div class="sum-stat">
                <div class="ss-icon">🎯</div>
                <div class="ss-val" data-count="94" data-suffix="%">0%</div>
                <div class="ss-label">AI Confidence</div>
              </div>
              <div class="sum-stat">
                <div class="ss-icon">📊</div>
                <div class="ss-val" data-count="247" data-suffix="">0</div>
                <div class="ss-label">Factors Analyzed</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>

  <script src="app.js"></script>
</body>
</html>
