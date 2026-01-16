document.addEventListener("DOMContentLoaded", () => {
  const events = document.querySelectorAll(".event");

  events.forEach((event, index) => {
    // Extract existing HTML content
    const title = event.querySelector(".title");
    const desc = event.querySelector(".desc");

    // Create new content wrapper
    const contentWrapper = document.createElement("div");
    contentWrapper.className = "content";
    contentWrapper.appendChild(title);
    contentWrapper.appendChild(desc);

    // Create connector line
    const connector = document.createElement("div");
    connector.className = "connector";

    // Clear original event
    event.innerHTML = "";

    // Alternate placement UP / DOWN
    if (index % 2 === 0) {
      event.classList.add("up");
      event.appendChild(contentWrapper);
      event.appendChild(connector);
    } else {
      event.classList.add("down");
      event.appendChild(connector);
      event.appendChild(contentWrapper);
    }
  });
});
