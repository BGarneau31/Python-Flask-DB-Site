
function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }
// fetching delete-workout views url to post a json with data then returns to specific page after the delete url function is executed
  function deleteWorkout(workoutId) {
    fetch("/delete-workout", {
      method: "POST",
      body: JSON.stringify({ workoutId: workoutId }),
    }).then((_res) => {
      window.location.href = "/workout";
    });
  }