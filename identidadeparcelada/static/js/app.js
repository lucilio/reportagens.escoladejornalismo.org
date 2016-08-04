$(document).foundation()
// SVG Buttons
window.addEventListener("load", bindSVGButtons, false);
function bindSVGButtons() {
    buttons=document.querySelector('[name=estilos-infografico]').getSVGDocument().querySelectorAll('g[id$="-button"]');
    for( i=0; i < buttons.length; i++ ) {
        /* console.log( buttons[i] ); */
        buttons[i].onclick = function( ev ){
            button = ev.currentTarget;
            modalId = button.id.replace( /([-_\w]+)-button$/, "#$1-modal" );
            $( modalId ).foundation('open');
        }
    }
}
