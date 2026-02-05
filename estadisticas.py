from estadisticas import registrar_resultado, ver_estadisticas

# registrar el examen
resultado = registrar_resultado(
    usuario_id=chat_id,
    unidad="U3",
    examen_num=1,
    respuestas_usuario=respuestas,
    TEMARIO=materia.TEMARIO
)

# mostrar estadísticas
bot.send_message(chat_id, ver_estadisticas(chat_id, "U3", 1))
