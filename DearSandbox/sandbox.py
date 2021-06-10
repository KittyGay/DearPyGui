import dearpygui.core as dpg
import dearpygui.simple as smpl
import dearpygui.contexts as cxt
import dearpygui.demo as demo

with cxt.font_registry():
    dpg.add_font("../../Resources/NotoSerifCJKjp-Medium.otf", 20, default_font=True)
    

main_texture_container = dpg.generate_uuid()

dpg.add_texture_container(id=main_texture_container)
dpg.add_static_texture(100, 100, [], parent=main_texture_container, file=dpg.mvFontAtlas, id=dpg.mvFontAtlas)

demo.show_demo()

smpl.start_dearpygui()