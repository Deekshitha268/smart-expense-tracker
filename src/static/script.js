async function loadExpenses(){

const response=await fetch("/expenses");

const expenses=await response.json();

const table=document.getElementById("expenseTable");

table.innerHTML="";

let total=0;

expenses.forEach(expense=>{

total+=expense.amount;

table.innerHTML+=`

<tr>

<td>${expense.id}</td>

<td>${expense.title}</td>

<td>${expense.amount}</td>

<td>${expense.category}</td>

<td>${expense.date}</td>

<td>

<button class="delete"

onclick="deleteExpense(${expense.id})">

Delete

</button>

</td>

</tr>

`;

});

document.getElementById("total").innerHTML=total;

}





async function addExpense(){

const expense={

title:document.getElementById("title").value,

amount:Number(document.getElementById("amount").value),

category:document.getElementById("category").value,

date:document.getElementById("date").value

};

await fetch("/expenses",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(expense)

});

document.getElementById("title").value="";

document.getElementById("amount").value="";

document.getElementById("category").value="";

document.getElementById("date").value="";

loadExpenses();

}

async function deleteExpense(id){

await fetch("/expenses/"+id,{

method:"DELETE"

});

loadExpenses();

}

loadExpenses();