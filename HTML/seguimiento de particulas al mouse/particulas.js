document.addEventListener("DOMContentLoaded", function() {
    const container = document.getElementById("particles-container");

    document.addEventListener("mousemove", function(event) {
        createParticle(event.clientX, event.clientY);
    });

    function createParticle(x, y) {
        const particle = document.createElement("div");
        particle.classList.add("particle");
        particle.style.left = x + "px";
        particle.style.top = y + "px";
        container.appendChild(particle);

        // Remove particle after a short delay
        setTimeout(() => {
            particle.remove();
        }, 2000);
    }
});
