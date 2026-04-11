import React, { useState } from 'react';
import { Shield, Brain, Zap, FileText, CheckCircle } from 'lucide-react';

const Dashboard = () => {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleAssessment = async () => {
    setLoading(true);
    // Simulate API call to FastAPI backend
    setTimeout(() => {
      setResult({
        riskScore: 24,
        status: "Low Risk",
        explanation: "Consistent income and clean medical history.",
        premium: 248
      });
      setLoading(false);
    }, 2000);
  };

  return (
    <div className="min-h-screen bg-[#020617] text-white p-8 font-sans">
      {/* Header */}
      <header className="flex justify-between items-center mb-12">
        <div className="flex items-center gap-2">
          <Shield className="text-indigo-500" size={32} />
          <h1 className="text-2xl font-bold italic">SureScore</h1>
        </div>
        <div className="px-4 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-500 text-xs font-bold uppercase tracking-widest">
          AI Engine Active
        </div>
      </header>

      <main className="grid lg:grid-cols-2 gap-8 max-w-6xl mx-auto">
        {/* Input Section */}
        <section className="bg-white/5 border border-white/10 p-8 rounded-2xl backdrop-blur-md">
          <h2 className="text-xl font-semibold mb-6 flex items-center gap-2">
            <FileText size={20} className="text-indigo-400" /> New Application
          </h2>
          <div className="space-y-4">
            <input type="text" placeholder="Applicant Name" className="w-full bg-slate-900 border border-slate-700 p-3 rounded-lg focus:outline-none focus:border-indigo-500" />
            <div className="grid grid-cols-2 gap-4">
              <input type="number" placeholder="Age" className="bg-slate-900 border border-slate-700 p-3 rounded-lg" />
              <input type="number" placeholder="Income (Annual)" className="bg-slate-900 border border-slate-700 p-3 rounded-lg" />
            </div>
            <div className="border-2 border-dashed border-slate-700 p-8 rounded-xl text-center text-slate-500 hover:border-indigo-500 transition-colors cursor-pointer">
              Upload Medical/Vehicle Reports (PDF)
            </div>
            <button 
              onClick={handleAssessment}
              disabled={loading}
              className="w-full bg-indigo-600 hover:bg-indigo-500 py-4 rounded-xl font-bold transition-all shadow-lg shadow-indigo-500/20"
            >
              {loading ? "AI Agents Processing..." : "Start Smart Assessment"}
            </button>
          </div>
        </section>

        {/* Results Section */}
        <section className="space-y-6">
          {result ? (
            <>
              <div className="bg-white/5 border border-white/10 p-6 rounded-2xl">
                <div className="flex justify-between items-start mb-4">
                  <span className="text-xs font-bold text-slate-500 uppercase tracking-widest">Risk Assessment</span>
                  <Brain className="text-pink-500" />
                </div>
                <div className="text-4xl font-bold mb-2">Score: {result.riskScore}<span className="text-lg text-slate-500">/100</span></div>
                <div className="inline-block px-3 py-1 rounded bg-emerald-500/20 text-emerald-400 text-xs font-bold uppercase">{result.status}</div>
              </div>

              <div className="bg-indigo-600/10 border border-indigo-500/30 p-6 rounded-2xl">
                <div className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-4">AI Explainability (SHAP)</div>
                <p className="text-slate-300 italic">"{result.explanation}"</p>
              </div>

              <div className="bg-white/5 border border-white/10 p-6 rounded-2xl flex justify-between items-center">
                <div>
                  <div className="text-xs font-bold text-slate-500 uppercase tracking-widest">Monthly Premium</div>
                  <div className="text-3xl font-bold text-cyan-400">${result.premium}</div>
                </div>
                <button className="bg-white text-black px-6 py-2 rounded-lg font-bold flex items-center gap-2">
                  <CheckCircle size={18} /> Approve Policy
                </button>
              </div>
            </>
          ) : (
            <div className="h-full border border-dashed border-slate-800 rounded-2xl flex items-center justify-center text-slate-600 italic text-center p-12">
              Waiting for data ingestion... <br/> Submit an application to see AI insights.
            </div>
          )}
        </section>
      </main>
    </div>
  );
};

export default Dashboard;
