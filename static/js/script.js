const searchInput = document.getElementById("search-name");
const searchButton = document.getElementById("search-button");
const profileInfo = document.querySelector(".profile-info");
const loadingMessage = document.getElementById("loading-message");
const nameDisplay = document.getElementById("name");
const summaryDisplay = document.getElementById("summary");
const factsList = document.getElementById("facts");
const avatar = document.querySelector(".avatar");

const resetUI = () => {
  profileInfo.hidden = true;
  loadingMessage.hidden = false;

  nameDisplay.textContent = "";
  summaryDisplay.textContent = "Loading...";
  factsList.innerHTML = "";
};

const displayProfile = ({ name, summary, facts, photo_url }) => {
  nameDisplay.textContent = name || "Name not found";
  summaryDisplay.textContent = summary || "Summary not available";
  factsList.innerHTML = (facts || []).map((f) => `<li>${f}</li>`).join("");

  avatar.src = photo_url || "https://via.placeholder.com/150";
  avatar.alt = name || "Profile Picture";

  loadingMessage.hidden = true;
  profileInfo.hidden = false;
};

const handleError = (message = "Error fetching data.") => {
  summaryDisplay.textContent = message;
  loadingMessage.hidden = true;
  profileInfo.hidden = false;
};

const fetchProfile = async (name) => {
  resetUI();

  try {
    const response = await fetch("/api/v1/summary", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name }),
    });

    if (!response.ok) return handleError("No data found.");

    const data = await response.json();
    displayProfile(data);
  } catch (error) {
    console.error("Error fetching data:", error);
    handleError();
  }
};

const handleSearch = () => {
  const name = searchInput.value.trim();
  if (!name) return alert("Please enter a name to search.");
  fetchProfile(name);
};

searchButton.addEventListener("click", handleSearch);

searchInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") handleSearch();
});
