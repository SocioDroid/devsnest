const main=document.querySelector(".main")

for(let i=0;i<400;i++)
{
    const items=document.createElement("div")
    items.addEventListener('click',()=>{
        if(items.style.backgroundColor!="white")
        items.style.backgroundColor="white";
        else
        items.style.background="brown";
    })
    main.appendChild(items)
}