// ===== Quiz Data =====
const quizData = [
    {
        question: "Inside which HTML element do we put the JavaScript?",
        options: [
            { text: "<script>", correct: true },
            { text: "<scripting>", correct: false },
            { text: "<javascript>", correct: false },
            { text: "<js>", correct: false },
        ]
    },
    {
        question: `What is the correct JavaScript syntax to change the content of the HTML element below?
        <p id="demo">This is a demonstration.</p>`,
        options: [
            { text: 'document.getElementByName("p").innerHTML = "Hello World!"', correct: false },
            { text: 'document.getElementById("demo").innerHTML = "Hello World!"', correct: true },
            { text: 'document.getElement("p").innerHTML = "Hello World!"', correct: false },
            { text: 'document.getElementbyclassName("p").innerHTML = "Hello World!"', correct: false },
        ]
    },
    {
        question: 'How do you write "Hello World" in an alert box?',
        options: [
            { text: 'msgBox("Hello World");', correct: false },
            { text: 'alertBox("Hello World");', correct: false },
            { text: 'alert("Hello World");', correct: true },
            { text: 'msg("Hello World");', correct: false },
        ]
    },
    {
        question: `What is the correct syntax for referring to an external script called "script.js"?`,
        options: [
            { text: `<script href="script.js">`, correct: false },
            { text: `<script src="script.js">`, correct: true },
            { text: `<script name="script.js">`, correct: false },
            { text: `<script alt="script.js">`, correct: false },
        ]
    },
    {
        question: "How to write an IF statement in JavaScript?",
        options: [
            { text: "if i = 5 then", correct: false },
            { text: "if i = 5", correct: false },
            { text: "if i == 5 then", correct: false },
            { text: "if (i == 5)", correct: true },
        ]
    },
    {
        question: "How does a FOR loop start?",
        options: [
            { text: "for (i = 0; i <= 5)", correct: false },
            { text: "for (i <= 5; i++)", correct: false },
            { text: "for i = 1 to 5", correct: false },
            { text: "for (i = 0; i <= 5; i++)", correct: true },
        ]
    },
    {
        question: "What is the correct way to write a JavaScript array?",
        options: [
            { text: 'var colors = ["red", "green", "blue"]', correct: true },
            { text: 'var colors = (1:"red", 2:"green", 3:"blue")', correct: false },
            { text: 'var colors = 1 = ("red"), 2 = ("green"), 3 = ("blue")', correct: false },
            { text: 'var colors = "red", "green", "blue"', correct: false },
        ]
    },
    {
        question: "How do you find the number with the highest value of x and y?",
        options: [
            { text: "Math.max(x, y)", correct: true },
            { text: "ceil(x, y)", correct: false },
            { text: "top(x, y)", correct: false },
            { text: "Math.ceil(x, y)", correct: false },
        ]
    },
    {
        question: 'How to write an IF statement for executing some code if "i" is NOT equal to 5?',
        options: [
            { text: 'if (i != 5)', correct: true },
            { text: 'if i <> 5', correct: false },
            { text: 'if (i <> 5)', correct: false },
            { text: 'if i =! 5 then', correct: false },
        ]
    },
    {
        question: "How do you round the number 7.25, to the nearest integer?",
        options: [
            { text: "round(7.25)", correct: false },
            { text: "Math.rnd(7.25)", correct: false },
            { text: "rnd(7.25)", correct: false },
            { text: "Math.round(7.25)", correct: true },
        ]
    }
]

// ===== DOM references =====
const startPage = document.getElementById("start_page");
const quizBody = document.getElementsByClassName("main_content")[0];
const scorePage = document.getElementById("score_page");

const revTime = document.getElementById("timer");
const questionElement = document.getElementById("question");
const optionsList = document.getElementById("options");
const questionCountEl = document.getElementById("questionCount");
const progressPercentEl = document.getElementById("progressPercent");
const progressFillEl = document.getElementById("progressFill");
const previousBtn = document.getElementById("previousBtn");
const nextBtn = document.getElementById("nextBtn");

const totalQuestionsValue = document.getElementById("totalQuestionsValue");
const correctValue = document.getElementById("correctValue");
const wrongValue = document.getElementById("wrongValue");
const timeLeftValue = document.getElementById("timeLeftValue");

// ===== Quiz state =====
const TOTAL_TIME = 600; // 10:00 in seconds
let currentQuestionIndex = 0;
let userAnswers = new Array(quizData.length).fill(null);
let totalSec = TOTAL_TIME;
let countdown = null;

// ===== Start / Restart =====
function quiz_start() {
    startPage.style.display = "none";
    scorePage.style.display = "none";
    quizBody.style.display = "flex";

    currentQuestionIndex = 0;
    userAnswers = new Array(quizData.length).fill(null);
    totalSec = TOTAL_TIME;

    updateTimerDisplay();
    startTimer();
    renderQuestion();
}

function restart_quiz() {
    quiz_start();
}

// ===== Timer =====
function startTimer() {
    if (countdown) clearInterval(countdown);

    countdown = setInterval(() => {
        totalSec--;

        if (totalSec < 0) {
            clearInterval(countdown);
            totalSec = 0;
            updateTimerDisplay();
            finishQuiz();
            return;
        }

        updateTimerDisplay();
    }, 1000);
}

function updateTimerDisplay() {
    let minutes = Math.floor(totalSec / 60);
    let seconds = totalSec % 60;

    minutes = String(minutes).padStart(2, "0");
    seconds = String(seconds).padStart(2, "0");

    revTime.innerHTML = `${minutes}:${seconds}`;
}

// ===== Render question =====
function renderQuestion() {
    const currentQuestion = quizData[currentQuestionIndex];

    // question text
    questionElement.innerText = currentQuestion.question;

    // options
    optionsList.innerHTML = "";
    currentQuestion.options.forEach((option, index) => {
        const li = document.createElement("li");
        li.innerText = option.text;
        li.setAttribute("data-index", index);

        if (userAnswers[currentQuestionIndex] === index) {
            li.classList.add("selected");
        }

        li.addEventListener("click", () => selectOption(index));
        optionsList.appendChild(li);
    });

    updateProgress();
    updateNavButtons();
}

function selectOption(index) {
    userAnswers[currentQuestionIndex] = index;
    renderQuestion();
}

// ===== Progress bar =====
function updateProgress() {
    const questionNumber = currentQuestionIndex + 1;
    const total = quizData.length;
    const percent = Math.round((questionNumber / total) * 100);

    questionCountEl.innerText = `Question ${questionNumber} of ${total}`;
    progressPercentEl.innerText = `${percent}% Complete`;
    progressFillEl.style.width = `${percent}%`;
}

// ===== Navigation buttons =====
function updateNavButtons() {
    previousBtn.disabled = currentQuestionIndex === 0;
    previousBtn.style.opacity = previousBtn.disabled ? "0.5" : "1";
    previousBtn.style.cursor = previousBtn.disabled ? "not-allowed" : "pointer";

    if (currentQuestionIndex === quizData.length - 1) {
        nextBtn.innerHTML = `Submit <i class="fa-solid fa-check"></i>`;
    } else {
        nextBtn.innerHTML = `Next <i class="fa-solid fa-arrow-right-long"></i>`;
    }
}

previousBtn.addEventListener("click", () => {
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        renderQuestion();
    }
});

nextBtn.addEventListener("click", () => {
    if (currentQuestionIndex < quizData.length - 1) {
        currentQuestionIndex++;
        renderQuestion();
    } else {
        finishQuiz();
    }
});

// ===== Finish quiz =====
function finishQuiz() {
    if (countdown) clearInterval(countdown);

    let correctCount = 0;
    let wrongCount = 0;

    quizData.forEach((question, index) => {
        const answerIndex = userAnswers[index];
        if (answerIndex === null) {
            wrongCount++;
            return;
        }
        if (question.options[answerIndex].correct) {
            correctCount++;
        } else {
            wrongCount++;
        }
    });

    totalQuestionsValue.innerText = quizData.length;
    correctValue.innerText = correctCount;
    wrongValue.innerText = wrongCount;

    let minutes = Math.floor(totalSec / 60);
    let seconds = totalSec % 60;
    minutes = String(minutes).padStart(2, "0");
    seconds = String(seconds).padStart(2, "0");
    timeLeftValue.innerText = `${minutes}:${seconds}`;

    quizBody.style.display = "none";
    scorePage.style.display = "flex";
}
