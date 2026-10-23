
const menuBtn = document.getElementById("menuBtn");
const nav = document.getElementById("nav");

// Navigasi untuk layar HP
menuBtn.addEventListener("click", () => {
  nav.classList.toggle("open");
  const isOpen = nav.classList.contains("open");
  menuBtn.setAttribute("aria-expanded", String(isOpen));
});

nav.querySelectorAll("a").forEach(link => {
  link.addEventListener("click", () => nav.classList.remove("open"));
});

// Filter timeline berdasarkan era AI
const filterButtons = document.querySelectorAll(".filter");
const events = document.querySelectorAll(".event");

filterButtons.forEach(button => {
  button.addEventListener("click", () => {
    filterButtons.forEach(item => item.classList.remove("active"));
    button.classList.add("active");

    const selectedEra = button.dataset.filter;

    events.forEach(event => {
      const shouldShow =
        selectedEra === "all" || event.dataset.era === selectedEra;

      event.classList.toggle("hidden", !shouldShow);
    });
  });
});

// Modal detail peristiwa
const modal = document.getElementById("modal");
const modalTitle = document.getElementById("modalTitle");
const modalInfo = document.getElementById("modalInfo");
const closeModalButton = document.getElementById("closeModal");
const doneModalButton = document.getElementById("doneModal");
let previousFocus = null;

function openModal(title, info) {
  previousFocus = document.activeElement;
  modalTitle.textContent = title;
  modalInfo.textContent = info;
  modal.classList.add("open");
  modal.setAttribute("aria-hidden", "false");
  document.body.style.overflow = "hidden";
  closeModalButton.focus();
}

function closeModal() {
  modal.classList.remove("open");
  modal.setAttribute("aria-hidden", "true");
  document.body.style.overflow = "";

  if (previousFocus) previousFocus.focus();
}

document.querySelectorAll(".detail-btn").forEach(button => {
  button.addEventListener("click", () => {
    openModal(button.dataset.title, button.dataset.info);
  });
});

closeModalButton.addEventListener("click", closeModal);
doneModalButton.addEventListener("click", closeModal);

modal.addEventListener("click", event => {
  if (event.target === modal) closeModal();
});

document.addEventListener("keydown", event => {
  if (event.key === "Escape" && modal.classList.contains("open")) {
    closeModal();
  }
});

// Animasi muncul saat elemen masuk ke layar
if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll(".event, .info-card").forEach(item => {
    observer.observe(item);
  });
}

console.log("AI Evolution website berhasil dijalankan.");
  