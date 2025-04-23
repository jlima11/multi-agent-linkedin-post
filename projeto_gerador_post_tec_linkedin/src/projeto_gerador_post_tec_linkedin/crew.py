from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ProjetoGeradorPostTecLinkedin():
    """ProjetoGeradorPostTecLinkedin crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def especialista_conteudo(self) -> Agent:
        return Agent(
        config=self.agents_config['especialista_conteudo'], 
        verbose=True
    )
    
    @agent
    def pesquisador_tecnico(self) -> Agent:
        return Agent(
        config=self.agents_config['pesquisador_tecnico'], 
        verbose=True
    )

    @agent
    def planner_conteudo(self) -> Agent:
        return Agent(
        config=self.agents_config['planner_conteudo'], 
        verbose=True
    )

    @agent
    def redator_tecnico(self) -> Agent:
        return Agent(
        config=self.agents_config['redator_tecnico'], 
        verbose=True
    )

    @agent
    def revisor_tecnico(self) -> Agent:
        return Agent(
        config=self.agents_config['revisor_tecnico'], 
        verbose=True
    )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def definir_tema(self) -> Task:
        return Task(
            config=self.tasks_config['definir_tema'],
        )

    @task
    def pesquisar_biblioteca(self) -> Task:
        return Task(
            config=self.tasks_config['pesquisar_biblioteca'],
        )

    @task
    def estruturar_conteudo(self) -> Task:
        return Task(
            config=self.tasks_config['estruturar_conteudo'],
        )

    @task
    def redigir_texto(self) -> Task:
        return Task(
            config=self.tasks_config['redigir_texto'],
        )

    @task
    def revisar_texto(self) -> Task:
        return Task(
            config=self.tasks_config['revisar_texto'],
            output_file='output/texto.txt',
        )
    @crew
    def crew(self) -> Crew:
        """Creates the ProjetoGeradorPostTecLinkedin crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
