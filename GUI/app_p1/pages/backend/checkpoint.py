#  # Set ERROR/INTERRUPTION status (testing)
#     def set_status_error(self):
#         current_gen_status = self.canvas.itemcget(self.gen_status_label, 'text')

#         if current_gen_status[:6] == 'ERROR:':
#             pass
#         else:
#             self.canvas.itemconfigure(self.gen_status_label, text='ERROR: KeyboardInterruption ')
        

#     # Visual Loading function

#     def process_tagging(self):
#         init_loading_bar = self.canvas.itemcget(self.loading_bar, 'text')

#         if len(init_loading_bar) != 0:
#             self.canvas.itemconfigure(self.loading_bar, text='')

#         self.canvas.itemconfigure(self.gen_status_label, text='Generating...')
#         self.update_label()


#     def update_label(self):
#         process_dummy = ['Obtaining Menu Item', 'Locating Category', 'Extracting Costs', 
#                     'Reading additional text elements', 'Locating Options', 'Finalizing Data Packet',
#                     'Entering into Excel', 'Verifying Format']

#         current_text = self.canvas.itemcget(self.loading_bar, 'text')
#         current_gen_status = self.canvas.itemcget(self.gen_status_label, 'text')

#         if current_gen_status[:6] == 'ERROR:':
#             updated_text = current_text + '|'
#             self.canvas.itemconfigure(self.loading_bar, text=updated_text)
#             pass

#         elif len(current_text) < 76:
#             self.generate_btn.config(state='disabled')
#             updated_text = current_text + "##"
#             self.canvas.itemconfigure(self.gen_status_label, text=process_dummy[len(current_text)%len(process_dummy)]+'...')
#             self.canvas.itemconfigure(self.loading_bar, text=updated_text)
#             self.window.after(50, self.update_label)

#         else:
#             self.canvas.itemconfigure(self.gen_status_label, text='Completed!')
#             self.generate_btn.config(state='active')