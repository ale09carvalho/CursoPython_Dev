import flet as ft

class TodoApp(ft.Column):
    
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="O que precisa ser feito?", expand=True, on_submit=self.add_clicked) # Campo de texto para digitar nova tarefa
        self.tasks = ft.Column() # Lista de tarefas

        # Abas para filtrar tarefas: todas, ativas, concluídas
        self.filter = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[ft.Tab(text="todas"), ft.Tab(text="pendente"), ft.Tab(text="finalizada")],
        )

        # Texto que mostra quantas tarefas ainda estão ativas
        self.items_left = ft.Text("0 itens restantes")

        self.width = 600
        
        # Layout principal do aplicativo
        self.controls = [
            # Título centralizado
            ft.Row(
                [ft.Text(value="TAREFAS", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            # Campo de entrada + botão adicionar
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD, on_click=self.add_clicked
                    ),
                ],
            ),
            # Filtro de abas + lista de tarefas + rodapé com contagem e botão limpar
            ft.Column(
                spacing=25,
                controls=[
                    self.filter,
                    self.tasks,
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            self.items_left,
                            ft.OutlinedButton(
                                text="Remover finalizadas", on_click=self.clear_clicked
                            ),
                        ],
                    ),
                ],
            ),
        ]

    # Atualiza a visualização da lista conforme a aba selecionada
    def tabs_changed(self, e):
        self.update()

    # Atualiza o status da tarefa (ativa/concluída)
    def task_status_change(self, e):
        self.update()

    # Adiciona nova tarefa
    def add_clicked(self, e):
        task = Task(self.new_task.value, self.task_status_change, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    # Remove tarefa específica
    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    # Remove todas as tarefas concluídas
    def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                self.task_delete(task)

    # Antes de atualizar a interface, ajusta visibilidade das tarefas e contagem
    def before_update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.tasks.controls:
            task.visible = (
                status == "todas"
                or (status == "pendente" and task.completed == False)
                or (status == "finalizada" and task.completed)
            )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count} item(s) pendente(s)"

class Task(ft.Column):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed = False # Estado inicial da tarefa: não concluída
        self.task_name = task_name # Nome da tarefa
        self.task_status_change = task_status_change # Função chamada quando marcar/desmarcar
        self.task_delete = task_delete # Função chamada quando excluir
        
        # Checkbox para marcar a tarefa como concluída
        self.display_task = ft.Checkbox(
            value=False, label=self.task_name, on_change=self.status_changed
        )
        
        # Campo de texto para editar o nome da tarefa
        self.edit_name = ft.TextField(expand=1, on_submit=self.save_clicked)

        # Layout para exibir a tarefa com checkbox e botões de editar/deletar
        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CREATE_OUTLINED,
                            tooltip="Editar",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.Icons.DELETE_OUTLINE,
                            tooltip="Deletar",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        # Layout para editar a tarefa (campo de texto + botão salvar)
        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.Colors.GREEN,
                    tooltip="Salvar",
                    on_click=self.save_clicked,
                ),
            ],
        )
        
        # A coluna conterá as duas views (exibição e edição)
        self.controls = [self.display_view, self.edit_view]

    # Abre um diálogo para editar o texto da tarefa
    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    # Função para salvar a edição
    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    # Remove a tarefa da lista
    def delete_clicked(self, e):
        self.task_delete(self)

    # Atualiza o status da tarefa (ativa/concluída)
    def status_changed(self, e):
        self.completed = self.display_task.value
        self.task_status_change(e)

def main(page: ft.Page):
    page.title = "App Gestor de Tarefas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # create application instance
    todo = TodoApp()

    # add application's root control to the page
    page.add(todo)

ft.app(main)