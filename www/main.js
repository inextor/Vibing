let wakeLock = null;

const requestWakeLock = async () => {
    try {
        wakeLock = await navigator.wakeLock.request('screen');
        console.log('Wake Lock activado!');
        wakeLock.addEventListener('release', () => {
            console.log('Wake Lock liberado!');
        });
    } catch (err) {
        console.error(`${err.name}, ${err.message}`);
    }
};

// --- Listeners de visibilidad y carga para WakeLock (no dependen del DOM) ---
document.addEventListener('visibilitychange', () => {
    if (wakeLock !== null && document.visibilityState === 'hidden') {
        wakeLock.release();
        wakeLock = null;
    }
    if (wakeLock === null && document.visibilityState === 'visible') {
        requestWakeLock();
    }
});

window.addEventListener('load', () => {
    requestWakeLock();
});

// --- Lógica principal que se ejecuta una vez que el DOM está listo ---
document.addEventListener('DOMContentLoaded', () => {

    // --- Lógica de Pantalla Completa ---
    const fullscreenToggleBtn = document.getElementById('fullscreen-toggle-btn');
    if (fullscreenToggleBtn) {
        const toggleFullscreen = () => {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen().catch(err => {
                    console.error(`Error al intentar entrar a pantalla completa: ${err.message} (${err.name})`);
                });
            } else {
                document.exitFullscreen();
            }
        };

        const updateFullscreenButton = () => {
            if (document.fullscreenElement) {
                fullscreenToggleBtn.textContent = 'Salir de Pantalla Completa';
                fullscreenToggleBtn.style.backgroundColor = '#1a1a1a';
            } else {
                fullscreenToggleBtn.textContent = 'Entrar a Pantalla Completa';
                fullscreenToggleBtn.style.backgroundColor = '#1a1a1a';
            }
        };

        fullscreenToggleBtn.addEventListener('click', toggleFullscreen);
        document.addEventListener('fullscreenchange', updateFullscreenButton);
        updateFullscreenButton(); // Llamada inicial
    }

    // --- Lógica de Botones Predefinidos ---
    const predefinedButtonsContainer = document.getElementById('predefined-buttons-container');
    if (predefinedButtonsContainer) {
        let buttons = JSON.parse(localStorage.getItem('predefinedButtons'));

        if (!buttons || buttons.length === 0) {
            buttons = [
                'git commit -m "feat: "',
                'git commit -m "fix: "',
                'git commit -m "docs: "',
                'git commit -m "style: "',
                'git commit -m "refactor: "',
                'git commit -m "test: "',
                'git commit -m "chore: "'
            ];
            localStorage.setItem('predefinedButtons', JSON.stringify(buttons));
        }

        buttons.forEach(buttonText => {
            const button = document.createElement('button');
            button.type = 'button';
            button.className = 'predefined-btn';
            button.textContent = buttonText;
            button.addEventListener('click', () => {
                const textArea = document.getElementById('text_area');
                textArea.value = button.textContent;
                textArea.focus();
            });
            predefinedButtonsContainer.appendChild(button);
        });
    }

    // --- Lógica de Envío con AJAX ---
    const form = document.querySelector('form');
    const textArea = document.getElementById('text_area');

    if (form && textArea) {
        form.addEventListener('submit', async (event) => {
            event.preventDefault();

            const action = document.activeElement.value;
            const text = textArea.value;

            if (!text) return;

            const formData = new URLSearchParams();
            formData.append('text_to_type', text);
            formData.append('action', action);

            try {
                const response = await fetch('/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: formData,
                });

                if (response.ok) {
                    console.log('Texto enviado correctamente.');
                    textArea.value = '';
                    textArea.focus();
                } else {
                    console.error('Error al enviar el texto.');
                }
            } catch (error) {
                console.error('Error de red:', error);
            }
        });
    }
});
