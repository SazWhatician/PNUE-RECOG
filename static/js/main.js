function initAnimations() {
    gsap.from(".reveal", {
        y: 50, opacity: 0, duration: 1.5, stagger: 0.2, ease: "power4.out"
    });

    const bar = document.getElementById('confBar');
    if (bar) {
        gsap.to(bar, {
            width: bar.getAttribute('data-value') + "%",
            duration: 2, ease: "expo.out", delay: 0.5
        });
    }
}

barba.init({
    transitions: [{
        leave(data) {
            return gsap.to(".transition-wipe", { y: "0%", duration: 0.8, ease: "expo.inOut" });
        },
        enter(data) {
            window.scrollTo(0, 0);
            initAnimations();
            return gsap.to(".transition-wipe", { y: "-100%", duration: 0.8, ease: "expo.inOut" });
        }
    }]
});

initAnimations();