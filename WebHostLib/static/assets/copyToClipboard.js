async function copyRoomToClipboard() {
  await navigator.clipboard.writeText(config['HOST_ADDRESS'] + ":" + room.last_port)
  document.getElementById("snackbar").classList.add("show");
  setTimeout(() => {
    document.getElementById("snackbar").classList.remove("show");
  }, 3000);
}