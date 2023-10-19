// document.addEventListener("DOMContentLoaded", () => {
//     if (
//         window.location.pathname.includes("daily") ||
//         window.location.pathname.includes("tag") ||
//         window.location.pathname.includes("reco")
//     ) {
//         document.getElementById("trade-button").classList.toggle("orange-text");
//     } else if (window.location.pathname == "/location/") {
//         document.getElementById("location-button").classList.toggle("orange-text");
//     }
// });

window.addEventListener('scroll', function() {
    // 현재 스크롤 위치를 가져옵니다.
    var scrollTop = window.scrollY;
    
    // 스크롤 위치가 100px 이상이면 클래스 스타일을 변경합니다.
    var element = document.querySelector('nav');
    var element2 = document.querySelector('.nav-buttons');
    if (element && scrollTop > 1) {
        element.style.color = 'white';
        
        element.style.backgroundColor = 'black';

    } else {
        // 스크롤 위치가 100px 미만이면 클래스 스타일을 복원합니다.
        element.style.color = 'black';
       
        element.style.backgroundColor = 'white';
    }
});