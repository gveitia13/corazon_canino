$('.ficha-details').on('click', function () {
  let id = this.id,
    params = new FormData()
  params.append('id', this.id)
  params.append('action', 'ficha-details')
  submit_with_ajax(location.pathname, params,
    response => {
      console.log(response)
      // $('#modal-esterilizado').attr('checked', false)
      document.querySelector('#ficha-image').src = response['foto']
      document.querySelector('#qr-image').src = response['qr']
      document.querySelector('#modal-name').innerText = response['nombre']
      document.querySelector('#modal-color').innerText = response['color']
      document.querySelector('#modal-iden').innerText = response['identidad']
      document.querySelector('#modal-peso').innerText = response['peso']
      document.querySelector('#modal-raza').innerText = response['raza']
      document.querySelector('#modal-sexo').innerText = response['sexo']
      document.querySelector('#modal-esterilizado').innerText = response['esterilizado']
/*      if (response.esterilizado ==='Si')
          $('#modal-esterilizado').attr('checked', true)*/
      $('#ficha-info').modal('show')
    })
})

  // $('.close').on('click', () => $('#myModalDetail').modal('hide'))