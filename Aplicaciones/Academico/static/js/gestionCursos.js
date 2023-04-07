(function(){
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

btnEliminacion.forEach(btn=>{
    btn.addEventListener('click',(e)=>{
        const confirmacion=confirm('¿Esta Seguro de Eliminar el campo?');
        if(!confirmacion){
            e.preventDefault();
        }
        
    } );
});

})();