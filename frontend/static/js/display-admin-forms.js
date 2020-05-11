const addevent = () =>{
   const addbtn=document.querySelector(".add");
   const addform=document.querySelector(".add-event-form-wrapper");

   addbtn.addEventListener('click', () => {
       addform.classList.toggle('active');
   });
}
addevent();