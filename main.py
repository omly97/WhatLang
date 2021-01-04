import click
from print_dict import pd
from app.modules.Dico import Dico
from app.modules.Database import Database
from app.modules.Printer import Printer


@click.group()
def cli():
    pass


@click.command()
@click.argument(
    'action', 
    type = click.Choice(['migrate', 'select-all', 'select-fr', 'select-ang', 'select-avg-fr', 'select-avg-ang'], case_sensitive = False),
    required = True
)
def db(action):
    if(action == 'migrate'):
        Database.migration()
        click.echo('Database migrate successfully !')

    elif(action == 'select-all'):
        Printer.print_proba(Database.select_all())

    elif(action == 'select-fr'):
        Printer.print_proba(Database.select_fr())

    elif(action == 'select-ang'):
        Printer.print_proba(Database.select_ang())

    elif(action == 'select-avg-fr'):
        Printer.print_avg(Database.select_avg_fr())

    elif(action == 'select-avg-ang'):
        Printer.print_avg(Database.select_avg_ang())


@click.command()
@click.argument('filename', type=click.Path(exists=True), required = True)
@click.option('-l', '--lang', type=click.Choice(['FR', 'ANG'], case_sensitive=True), required=True, help='Langue du fichier')
def learn(filename, lang):
    click.echo("Loading ............")
    dict_occ = Dico.get_occurrences_of_file(filename)
    dict_prob = Dico.dict_probability_of(dict_occ)
    Database.insert(lang, dict_prob)
    click.echo("Data saved successfully !")


@click.command()
@click.argument('filename', type=click.Path(exists=True), required = True)
def whatlang(filename):
    click.echo("Loading ............")

    # file probality
    dict_occ = Dico.get_occurrences_of_file(filename)
    dict_proba = Dico.dict_probability_of(dict_occ)
    click.echo("\n >>> Probabilité du texte")
    pd(dict_proba)

    # compare french probability
    dict_avr_fr = Dico.dict_of_row((Database.select_avg_fr()))
    dict_diff_fr = Dico.diff_dict(dict_avr_fr, dict_proba)
    click.echo("\n >>> Comparaison avec texte francais")
    pd(dict_diff_fr)

    # compare english probability
    dict_avr_ang = Dico.dict_of_row(Database.select_avg_ang())
    dict_diff_ang = Dico.diff_dict(dict_avr_ang, dict_proba)
    click.echo("\n >>> Comparaison avec texte anglais")
    pd(dict_diff_ang)


cli.add_command(db)
cli.add_command(learn)
cli.add_command(whatlang)


if __name__ == '__main__':
    cli()
