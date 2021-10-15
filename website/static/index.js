function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId }),
  }).then((response) => {
    window.location.href = "/";
  });
}
