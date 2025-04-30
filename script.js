VANTA.NET({
    el: "#vanta-bg",
    mouseControls: true,
    touchControls: true,
    minHeight: 200.00,
    minWidth: 200.00,
    scale: 1.00,
    scaleMobile: 1.00,
    color: 0x0ff,
    backgroundColor: 0x111111
  });
  
  function addPair() {
    const container = document.getElementById('teacher-subject-container');
    const div = document.createElement('div');
    div.classList.add('pair');
    div.innerHTML = `
      <input type="text" name="teacher[]" placeholder="Teacher Name" required>
      <input type="text" name="subject[]" placeholder="Subject" required>
    `;
    container.appendChild(div);
  }
  