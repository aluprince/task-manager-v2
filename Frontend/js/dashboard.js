// Fake Data
const projects = [
  {
    id: 1,
    name: "Website Redesign",
    description: "Update branding and UX",
    deadline: "2025-10-10",
    status: "In Progress",
    tasks: [
      { id: 1, name: "Wireframes", completed: true },
      { id: 2, name: "Prototype", completed: false },
    ]
  },
  {
    id: 2,
    name: "Mobile App",
    description: "Build MVP for iOS",
    deadline: "2025-11-01",
    status: "Pending",
    tasks: [
      { id: 1, name: "UI Design", completed: false },
      { id: 2, name: "API Integration", completed: false },
    ]
  }
];

const tasks = [
  { id: 1, name: "Buy groceries", completed: false },
  { id: 2, name: "Finish homework", completed: true },
];

// Sections
function renderProjects() {
  return `
    <h1>📂 Projects</h1>
    ${projects.map(p => `
      <div class="project-card">
        <h2>${p.name}</h2>
        <p>${p.description}</p>
        <p><b>Deadline:</b> ${p.deadline}</p>
        <p><b>Status:</b> ${p.status}</p>
        <button onclick="toggleTasks(${p.id})">View Tasks</button>
        <div id="tasks-${p.id}" class="hidden tasks-list">
          ${p.tasks.map(t => `
            <div>
              <input type="checkbox" ${t.completed ? "checked" : ""}/> ${t.name}
            </div>
          `).join("")}
        </div>
      </div>
    `).join("")}
  `;
}

function toggleTasks(projectId) {
  const el = document.getElementById(`tasks-${projectId}`);
  el.classList.toggle("hidden");
}

function renderTasks() {
  return `
    <h1>✅ Independent Tasks</h1>
    ${tasks.map(t => `
      <div>
        <input type="checkbox" ${t.completed ? "checked" : ""}/> ${t.name}
      </div>
    `).join("")}
  `;
}

function renderGoals() {
  return `
    <h1>🎯 Goals (Pro Feature)</h1>
    <div class="goals-coming-soon">
      <p>Premium Productivity Tools Coming Soon...</p>
      <ul>
        <li>📆 Timelines</li>
        <li>📂 Advanced Projects</li>
        <li>⏰ Smart Reminders</li>
        <li>⚡ Nudges</li>
        <li class="locked">🤖 Brainstorming Chatbot</li>
        <li class="locked">📝 Whiteboard</li>
      </ul>
    </div>
  `;
}

function renderSettings() {
  return `
    <h1>⚙️ Settings</h1>
    <form class="settings-form">
      <label>Update Profile</label>
      <input type="text" placeholder="Name"/>
      <input type="email" placeholder="Email"/>
      <button type="button">Save</button>
    </form>
    <button class="reset-btn">Reset Password</button>
    <button class="logout-btn">Logout</button>
  `;
}

// Router
const content = document.getElementById("content");
const routes = {
  projects: renderProjects,
  tasks: renderTasks,
  goals: renderGoals,
  settings: renderSettings,
};

document.querySelectorAll(".sidebar li").forEach(li => {
  li.addEventListener("click", () => {
    const section = li.dataset.section;
    content.innerHTML = routes[section]();
  });
});

// Default
content.innerHTML = renderProjects();
