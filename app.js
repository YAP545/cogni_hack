// ── Particle Canvas (SAFE VERSION) ─────────────────────────────
(function initParticles() {

  const canvas = document.getElementById('particleCanvas');

  // 🔴 FIX: Prevent crash if canvas not found
  if (!canvas) return;

  const ctx = canvas.getContext('2d');

  let W, H, particles = [], animId;

  function resize() {
    W = canvas.width = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }

  class Particle {
    constructor() {
      this.reset();
    }

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
      this.x += this.vx;
      this.y += this.vy;

      if (this.x < 0 || this.x > W || this.y < 0 || this.y > H) {
        this.reset();
      }
    }

    draw() {
      ctx.save();
      ctx.globalAlpha = this.alpha;
      ctx.fillStyle = this.color;

      ctx.shadowBlur = 8;
      ctx.shadowColor = this.color;

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

    particles.forEach(p => {
      p.update();
      p.draw();
    });

    drawConnections();
  }

  window.addEventListener('resize', resize);
  window.addEventListener('load', init);

})();
