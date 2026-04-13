const API = "http://127.0.0.1:5000"

async function criar() {
    const nome = document.getElementById("nome").value
    const idade = document.getElementById("idade").value

    if (!nome || !idade) {
        alert("Preencha os campos!")
        return
    }

    await fetch(API + "/customers", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ nome, idade: Number(idade) })
    })

    listar()
}

async function listar() {
    const res = await fetch(API + "/customers")
    const data = await res.json()
    renderTabela(data)
}

async function buscarIntervalo() {
    const inicio = document.getElementById("inicio").value
    const fim = document.getElementById("fim").value

    if (!inicio || !fim) {
        alert("Informe os IDs!")
        return
    }

    const res = await fetch(`${API}/customers/range?inicio=${inicio}&fim=${fim}`)
    const data = await res.json()

    renderTabela(data)
}

function renderTabela(data) {
    const tabela = document.getElementById("tabela")
    tabela.innerHTML = ""

    data.forEach(c => {
        const tr = document.createElement("tr")

        tr.innerHTML = `
            <td>${c.id}</td>
            <td>${c.nome}</td>
            <td>${c.idade} anos</td>
            <td>
                <button class="edit" onclick="editar(${c.id})">Editar</button>
                <button class="delete" onclick="deletar(${c.id})">Excluir</button>
            </td>
        `

        tabela.appendChild(tr)
    })
}

async function deletar(id) {
    await fetch(API + "/customers/" + id, { method: "DELETE" })
    listar()
}

async function editar(id) {
    const novaIdade = prompt("Nova idade:")

    if (!novaIdade) return

    await fetch(API + "/customers/" + id, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ idade: Number(novaIdade) })
    })

    listar()
}
async function limpar() {
    const confirmacao = confirm("Tem certeza que deseja apagar TODOS os clientes?")

    if (!confirmacao) return

    await fetch(API + "/customers/clear", {
        method: "DELETE"
    })

    listar()
}

// IMPORTAR
document.getElementById("fileInput").addEventListener("change", async function () {
    const file = this.files[0]

    if (!file) return

    const formData = new FormData()
    formData.append("file", file)

    await fetch(API + "/customers/upload", {
        method: "POST",
        body: formData
    })

    alert("Arquivo importado com sucesso!")

    listar()
})

// EXPORTAR
function exportar() {
    window.open(API + "/customers/export", "_blank")
}