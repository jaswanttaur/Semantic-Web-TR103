// const setMusic = (i) => {
//     seekBar.value = 0;
//     let song = song[i];
//     currentMusic = i;
//     music.src = song.path;

//     songName.innerHTML = song.name;
//     artistName.innerHTML = song.artist;
//     currentTime.innerHTML = '00:00';
//     setTimeout(() => {
//         seekBar.max = music.duration;
//         console.log(music.duration);
// }, 300);
// }
document.addEventListener('DOMContentLoaded', function() {
    const audio = document.getElementById('audio');
    const playPauseBtn = document.querySelector('.play-pause-btn');

    let isPlaying = false;

    // Play or pause audio
    function togglePlayPause() {
        if (isPlaying) {
            audio.pause();
            playPauseBtn.textContent = 'Play';
        } else {
            audio.play();
            playPauseBtn.textContent = 'Pause';
        }
        isPlaying = !isPlaying;
    }

    // Update play/pause button text based on audio state
    audio.addEventListener('play', function() {
        isPlaying = true;
        playPauseBtn.textContent = 'Pause';
    });

    audio.addEventListener('pause', function() {
        isPlaying = false;
        playPauseBtn.textContent = 'Play';
    });

    // Event listener for play/pause button click
    playPauseBtn.addEventListener('click', togglePlayPause);
});
