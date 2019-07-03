function closesorturl() 
{
    document.getElementById("sorturl").style.width = "0%";
    document.getElementById("sorturl").style.height = "0%"; 
}
function opensorturl() 
{
    document.getElementById("sorturl").style.width = "100%";
    document.getElementById("sorturl").style.height = "100%";
}
                    
function closesignin() 
{
    document.getElementById("signin").style.width = "0%";
    document.getElementById("signin").style.height = "0%";
}
function opensignin() 
{
    document.getElementById("signin").style.width = "100%";
    document.getElementById("signin").style.height = "100%";
    document.getElementById("mySidenav").style.width = "0%";
}
                    
                    
function closesignup() 
{
    document.getElementById("signup").style.width = "0%";
    document.getElementById("signup").style.height = "0%";
}
function opensignup() 
{
    document.getElementById("signup").style.width = "100%";
    document.getElementById("signup").style.height = "100%";
    document.getElementById("mySidenav").style.width = "0%";
}
                    
function openNav() 
{
    document.getElementById("mySidenav").style.width = "20%";
}
                        
function closeNav() 
{
    document.getElementById("mySidenav").style.width = "0%";
}

function copy(str)
{
    var el = document.createElement('textarea');
    el.value = str;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy')
    document.body.removeChild(el);
    window.alert('copied:'+str);
}