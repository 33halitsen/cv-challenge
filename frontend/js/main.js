async function getVisitorCount() {
    const isEnglish = document.documentElement.lang === "en";
    const endpoint = isEnglish
        ? "https://di28c27k1xspi.cloudfront.net/visitorcounter_english"
        : "https://di28c27k1xspi.cloudfront.net/visitorcounter";

    try {
        let response = await fetch(endpoint);
        let data = await response.json();
        const counterElement = document.getElementById("visitor-count");
        if (counterElement) {
            counterElement.innerText = data.visit_count;
        }
    } catch (error) {
        console.error("Sayaç yüklenirken hata oluştu / Error loading counter:", error);
        const counterElement = document.getElementById("visitor-count");
        if (counterElement) {
            counterElement.innerText = "—";
        }
    }
}

document.addEventListener("DOMContentLoaded", getVisitorCount);