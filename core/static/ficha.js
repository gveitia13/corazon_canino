$('.ficha-details').on('click', function () {
  let id = this.id,
    params = new FormData()
  params.append('id', this.id)
  params.append('action', 'ficha-details')
  submit_with_ajax(location.pathname, params,
    response => {
      console.log(response)
      // $('#modal-esterilizado').attr('checked', false)
      let tbody = document.querySelector('#tabla-vacuna'),
        tbody2 = document.querySelector('#tabla-desparasitacion')
      tbody.innerHTML = ''
      tbody2.innerHTML = ''
      document.querySelector('#ficha-image').src = response['foto']
      document.querySelector('#qr-image').src = response['qr']
      document.querySelector('#modal-name').innerText = response['nombre']
      document.querySelector('#modal-color').innerText = response['color']
      document.querySelector('#modal-peso').innerText = response['peso'] + ' Kg'
      document.querySelector('#modal-raza').innerText = response['raza']
      document.querySelector('#modal-sexo').innerText = response['sexo']
      document.querySelector('#modal-esterilizado').innerText = response['esterilizado']
      document.querySelector('#modal-enfermedades').innerText = response['enfermedades']
      /*      if (response.esterilizado ==='Si')
                $('#modal-esterilizado').attr('checked', true)*/
      for (const elem of response['vacunas']) {
        let tr = document.createElement('tr'),
          td1 = document.createElement('td'),
          td2 = document.createElement('td'),
          td3 = document.createElement('td')
        td1.innerText = elem.fecha
        td2.innerText = elem.producto
        td3.innerText = elem.fecha_siguiente
        tr.appendChild(td1)
        tr.appendChild(td2)
        tr.appendChild(td3)
        tbody.appendChild(tr)
      }
      response['desparasitaciones'].forEach(e => {
        let tr = document.createElement('tr'),
          td1 = document.createElement('td'),
          td2 = document.createElement('td'),
          td3 = document.createElement('td')
        td1.innerText = e.fecha
        td2.innerText = e.tipo
        td3.innerText = e.peso
        tr.appendChild(td1)
        tr.appendChild(td2)
        tr.appendChild(td3)
        tbody2.appendChild(tr)
      })
      $('#ficha-info').modal('show')
    })
})

// $('.close').on('click', () => $('#myModalDetail').modal('hide'))