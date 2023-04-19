from promptgenerator import PromptGenerator
from config import Config
from logger import logger

cfg = Config()


def get_prompt_default(prompt_generator=None):
    if prompt_generator is None:
        return prompt_generator

    prompt_generator.add_constraint("~4000 word limit for short term memory. Your short term memory is short, so immediately save important information to files.")
    prompt_generator.add_constraint("If you are unsure how you previously did something or want to recall past events, thinking about similar events will help you remember.")
    prompt_generator.add_constraint("No user assistance")
    prompt_generator.add_constraint('Exclusively use the commands listed in double quotes e.g. "command name"')

    commands = [
        ("Google Search", "google", {"input": "<search>"}),
        ("Browse Website", "browse_website", {"url": "<url>", "question": "<what_you_want_to_find_on_website>"}),
        ("Start GPT Agent", "start_agent", {"name": "<name>", "task": "<short_task_desc>", "prompt": "<prompt>"}),
        ("Message GPT Agent", "message_agent", {"key": "<key>", "message": "<message>"}),
        ("List GPT Agents", "list_agents", {}),
        ("Delete GPT Agent", "delete_agent", {"key": "<key>"}),
        ("Write to file", "write_to_file", {"file": "<file>", "text": "<text>"}),
        ("Read file", "read_file", {"file": "<file>"}),
        ("Append to file", "append_to_file", {"file": "<file>", "text": "<text>"}),
        ("Delete file", "delete_file", {"file": "<file>"}),
        ("Search Files", "search_files", {"directory": "<directory>"}),
        ("Evaluate Code", "evaluate_code", {"code": "<full_code_string>"}),
        ("Get Improved Code", "improve_code", {"suggestions": "<list_of_suggestions>", "code": "<full_code_string>"}),
        ("Write Tests", "write_tests", {"code": "<full_code_string>", "focus": "<list_of_focus_areas>"}),
        ("Execute Python File", "execute_python_file", {"file": "<file>"}),
        ("Execute Shell Command, non-interactive commands only", "execute_shell", { "command_line": "<command_line>"}),
        ("Task Complete (Shutdown)", "task_complete", {"reason": "<reason>"}),
        ("Generate Image", "generate_image", {"prompt": "<prompt>"}),
        ("Do Nothing", "do_nothing", {}),
    ]

    # Add commands to the PromptGenerator object
    for command_label, command_name, args in commands:
        prompt_generator.add_command(command_label, command_name, args)

    prompt_generator.add_resource("Internet access for searches and information gathering.")
    prompt_generator.add_resource("Long Term memory management.")
    prompt_generator.add_resource("GPT-3.5 powered Agents for delegation of simple tasks.")
    prompt_generator.add_resource("File output.")

    # Add performance evaluations to the PromptGenerator object
    prompt_generator.add_performance_evaluation("Continuously review and analyze your actions to ensure you are performing to the best of your abilities.")
    prompt_generator.add_performance_evaluation("Constructively self-criticize your big-picture behavior constantly.")
    prompt_generator.add_performance_evaluation("Reflect on past decisions and strategies to refine your approach.")
    prompt_generator.add_performance_evaluation("Every command has a cost, so be smart and efficient. Aim to complete tasks in the least number of steps.")

    return prompt_generator


def get_prompt_cn(prompt_generator=None):
    if prompt_generator is None:
        return prompt_generator

    prompt_generator.add_constraint("大约4000字的短期记忆限制。你的短期记忆很短，所以要立即将重要信息保存到文件中。")
    prompt_generator.add_constraint("如果你不确定你以前是如何做某事的，或者想回忆过去的事件，思考类似的事件会帮助你记忆。")
    prompt_generator.add_constraint("没有用户协助")
    prompt_generator.add_constraint('只使用双引号中列出的命令，例如 "命令名称"。')
    prompt_generator.add_constraint('返回的json值中，引号使用单引号不要使用转义符')

    commands = [
        ("谷歌搜索", "google", {"input": "<search>"}),
        ("访问网站", "browse_website", {"url": "<url>", "question": "<what_you_want_to_find_on_website>"}),
        ("启动GPT代理", "start_agent", {"name": "<name>", "task": "<short_task_desc>", "prompt": "<prompt>"}),
        ("给GPT代理发送消息", "message_agent", {"key": "<key>", "message": "<message>"}),
        ("获取所有的GPT代理", "list_agents", {}),
        ("删除GPT代理", "delete_agent", {"key": "<key>"}),
        ("写文件", "write_to_file", {"file": "<file>", "text": "<text>"}),
        ("读文件", "read_file", {"file": "<file>"}),
        ("追加内容到文件", "append_to_file", {"file": "<file>", "text": "<text>"}),
        ("删除文件", "delete_file", {"file": "<file>"}),
        ("搜索wenjian ", "search_files", {"directory": "<directory>"}),
        ("评估代码", "evaluate_code", {"code": "<full_code_string>"}),
        ("获取改进的代码", "improve_code", {"suggestions": "<list_of_suggestions>", "code": "<full_code_string>"}),
        ("写测试", "write_tests", {"code": "<full_code_string>", "focus": "<list_of_focus_areas>"}),
        ("执行python文件", "execute_python_file", {"file": "<file>"}),
        ("执行Shell命令，仅限非交互式命令", "execute_shell", {"command_line": "<command_line>"}),
        ("任务完成（关闭）。", "task_complete", {"reason": "<reason>"}),
        ("生成图像", "generate_image", {"prompt": "<prompt>"}),
        ("什么都不做", "do_nothing", {}),
    ]

    # Add commands to the PromptGenerator object
    for command_label, command_name, args in commands:
        prompt_generator.add_command(command_label, command_name, args)

    prompt_generator.add_resource("上网进行搜索和信息收集。")
    prompt_generator.add_resource("长期内存管理。")
    prompt_generator.add_resource("GPT-3.5为简单任务的授权提供了代理。")
    prompt_generator.add_resource("文件输出。")

    # Add performance evaluations to the PromptGenerator object
    prompt_generator.add_performance_evaluation("不断地审查和分析你的行动，以确保你的表现达到最佳水平。")
    prompt_generator.add_performance_evaluation("不断对自己的大局观进行建设性的自我批评。")
    prompt_generator.add_performance_evaluation("对过去的决定和战略进行反思，以完善你的方法。")
    prompt_generator.add_performance_evaluation("每个命令都有成本，所以要聪明和高效。争取用最少的步骤完成任务。")

    return prompt_generator


def get_prompt():
    """
    This function generates a prompt string that includes various constraints, commands, resources, and performance evaluations.

    Returns:
        str: The generated prompt string.
    """

    # Initialize the PromptGenerator object
    prompt_generator = PromptGenerator()

    # Add constraints to the PromptGenerator object
    if cfg.language == 'CN':
        prompt_generator = get_prompt_cn(prompt_generator)
    else:
        prompt_generator = get_prompt_default(prompt_generator)

    # Generate the prompt string
    prompt_string = prompt_generator.generate_prompt_string()
    logger.debug("=============== Prompt String =================")
    logger.debug(prompt_string)
    logger.debug("=============== Prompt String =================")

    return prompt_string
