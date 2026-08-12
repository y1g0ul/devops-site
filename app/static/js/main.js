const terminalReplies = {
  help: ["commands: whoami, skills, experience, education, contact, clear"],
  whoami: [
    "nikita — junior devops / system administration",
    "location: moscow | status: learning",
  ],
  skills: [
    "linux  docker  docker-compose  git",
    "bash  python  sql  github-actions  gitlab-ci",
  ],
  experience: [
    "ГВЦ РЖД — стажёр / техник 1 категории",
    "automation: FTP changes → eXpress notifications",
  ],
  education: [
    "Московский индустриальный колледж",
    "Информационные системы и программирование · 2024",
  ],
  contact: [
    "github: y1g0ul",
    "telegram: @y1g0ul",
    "email: markzerone1@gmail.com",
  ],
};

const terminalForm = document.querySelector("#terminal-form");
const terminalInput = document.querySelector("#terminal-command");
const terminalOutput = document.querySelector("#terminal-output");
const clearButton = document.querySelector("#terminal-clear");
const commandButtons = document.querySelectorAll("[data-command]");

function addTerminalLine(type, value) {
  const line = document.createElement("p");
  const marker = document.createElement("span");

  line.className = `terminal-line terminal-line--${type}`;
  marker.textContent = type === "command" ? "$ " : type === "error" ? "! " : "› ";
  line.append(marker, document.createTextNode(value));
  terminalOutput.append(line);
}

function clearTerminal() {
  terminalOutput.replaceChildren();
}

function runTerminalCommand(rawCommand) {
  const command = rawCommand.trim().toLowerCase();
  if (!command) return;

  if (command === "clear") {
    clearTerminal();
    return;
  }

  addTerminalLine("command", rawCommand.trim());

  const reply = terminalReplies[command];
  if (reply) {
    reply.forEach((line) => addTerminalLine("reply", line));
  } else {
    addTerminalLine("error", `command not found: ${command}. try 'help'`);
  }

  terminalOutput.scrollTo({
    top: terminalOutput.scrollHeight,
    behavior: reducedMotion ? "auto" : "smooth",
  });
}

terminalForm?.addEventListener("submit", (event) => {
  event.preventDefault();
  runTerminalCommand(terminalInput.value);
  terminalInput.value = "";
});

clearButton?.addEventListener("click", () => {
  clearTerminal();
  terminalInput.focus();
});

commandButtons.forEach((button) => {
  button.addEventListener("click", () => {
    runTerminalCommand(button.dataset.command ?? "");
    terminalInput.focus();
  });
});

const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (!reducedMotion && "IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { rootMargin: "0px 0px -8%", threshold: 0.08 },
  );

  document.querySelectorAll(".content-section").forEach((section) => {
    section.classList.add("reveal-ready");
    observer.observe(section);
  });
}
